#!/usr/bin/env python3
"""
Musik-Generierung für Mammutprojekt mit MusicGen
Atmosphärische Soundtracks mit klassischen Instrumenten
"""

from transformers import AutoProcessor, MusicgenForConditionalGeneration
import scipy.io.wavfile
from pathlib import Path
import torch

# Output-Verzeichnis
OUTPUT_DIR = Path(__file__).parent.parent / "audio" / "music"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Musik-Stücke nach Stimmung
TRACKS = {
    # === FRIEDLICH / HOFFNUNG ===
    "peaceful_home": {
        "prompt": "gentle piano and violin, warm domestic atmosphere, 1930s style, nostalgic, soft, peaceful family moment",
        "duration": 15  # Sekunden
    },
    "hope_theme": {
        "prompt": "hopeful orchestral strings, gentle cello melody, rising hope, tender, emotional, classical style",
        "duration": 12
    },
    "childhood_innocence": {
        "prompt": "light playful piano, innocent childhood melody, gentle flute, nostalgic, bittersweet, 1930s style",
        "duration": 10
    },
    
    # === SPANNUNG / BEDROHUNG ===
    "tension_rising": {
        "prompt": "dark orchestral tension, low strings tremolo, ominous atmosphere, suspenseful, building dread, classical",
        "duration": 15
    },
    "danger_approaching": {
        "prompt": "urgent strings, dramatic timpani, threatening brass, Nazi era tension, dark classical, impending doom",
        "duration": 12
    },
    "hiding_fear": {
        "prompt": "quiet tense strings, heartbeat rhythm, fearful atmosphere, holding breath, minimal classical, suspense",
        "duration": 15
    },
    
    # === TRAUER / VERLUST ===
    "loss_grief": {
        "prompt": "sorrowful violin solo, mourning cello, deep grief, slow tempo, funeral classical, devastating loss",
        "duration": 20
    },
    "farewell": {
        "prompt": "melancholic piano, goodbye theme, tearful strings, separation, bittersweet farewell, emotional classical",
        "duration": 15
    },
    "aftermath_silence": {
        "prompt": "sparse piano notes, empty silence between, devastation aftermath, hollow, minimal classical, shock",
        "duration": 12
    },
    
    # === CHAOS / GEWALT ===
    "kristallnacht_chaos": {
        "prompt": "chaotic orchestral, dissonant strings, violent brass, breaking glass atmosphere, terrifying, dramatic classical",
        "duration": 15
    },
    "mob_violence": {
        "prompt": "aggressive percussion, threatening brass fanfare, mob mentality, propaganda style, ominous march",
        "duration": 12
    },
    
    # === MUT / WIDERSTAND ===
    "courage_theme": {
        "prompt": "brave orchestral theme, determined strings, quiet heroism, moral courage, hopeful undertone, classical",
        "duration": 12
    },
    "small_act_of_kindness": {
        "prompt": "gentle hopeful piano, warm strings swell, humanity in darkness, tender moment, classical redemption",
        "duration": 10
    },
    
    # === REFLEXION ===
    "reflection_guilt": {
        "prompt": "contemplative piano, regretful cello, moral weight, guilt and reflection, slow classical, introspective",
        "duration": 15
    },
    "never_forget": {
        "prompt": "solemn orchestral, memorial theme, remembrance, dignified strings, honoring victims, classical requiem style",
        "duration": 20
    }
}

def load_model():
    """Lade MusicGen-Medium Modell"""
    print("🎵 Lade MusicGen-Medium...")
    processor = AutoProcessor.from_pretrained("facebook/musicgen-medium")
    model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-medium")
    
    # GPU wenn verfügbar
    if torch.cuda.is_available():
        model = model.to("cuda")
        print("  → GPU aktiviert")
    
    return processor, model

def generate_track(processor, model, track_id: str, track_data: dict):
    """Generiere einen Musik-Track"""
    prompt = track_data["prompt"]
    duration = track_data["duration"]
    
    print(f"  Generiere: {track_id} ({duration}s)")
    
    # Tokens berechnen (MusicGen: ~50 tokens = 1 Sekunde bei 32kHz)
    max_tokens = duration * 50
    
    inputs = processor(
        text=[prompt],
        padding=True,
        return_tensors="pt"
    )
    
    if torch.cuda.is_available():
        inputs = inputs.to("cuda")
    
    audio_values = model.generate(**inputs, max_new_tokens=max_tokens)
    
    # Sample rate von MusicGen
    sampling_rate = model.config.audio_encoder.sampling_rate
    
    # Speichern als WAV
    audio_data = audio_values[0, 0].cpu().numpy()
    output_path = OUTPUT_DIR / f"{track_id}.wav"
    scipy.io.wavfile.write(output_path, rate=sampling_rate, data=audio_data)
    
    print(f"  ✓ Gespeichert: {output_path}")
    return output_path

def main():
    print("=" * 50)
    print("  Mammutprojekt - Musik-Generierung")
    print("=" * 50)
    
    processor, model = load_model()
    
    generated = []
    for track_id, track_data in TRACKS.items():
        try:
            path = generate_track(processor, model, track_id, track_data)
            generated.append({"id": track_id, "path": str(path)})
        except Exception as e:
            print(f"  ✗ Fehler bei {track_id}: {e}")
    
    print(f"\n✓ {len(generated)} Tracks generiert!")
    
    # Übersicht
    print("\n📋 Track-Übersicht:")
    print("-" * 40)
    categories = {
        "Friedlich": ["peaceful_home", "hope_theme", "childhood_innocence"],
        "Spannung": ["tension_rising", "danger_approaching", "hiding_fear"],
        "Trauer": ["loss_grief", "farewell", "aftermath_silence"],
        "Chaos": ["kristallnacht_chaos", "mob_violence"],
        "Mut": ["courage_theme", "small_act_of_kindness"],
        "Reflexion": ["reflection_guilt", "never_forget"]
    }
    for cat, tracks in categories.items():
        print(f"\n  {cat}:")
        for t in tracks:
            if t in [g["id"] for g in generated]:
                print(f"    ✓ {t}")

if __name__ == "__main__":
    main()
