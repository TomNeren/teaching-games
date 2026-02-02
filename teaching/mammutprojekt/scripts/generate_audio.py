#!/usr/bin/env python3
"""
Audio-Generierung für die NS-Simulation mit Bark
Generiert Erzählerstimmen und Soundeffekte
"""

import os
import sys
import json
from pathlib import Path

# Add venv to path
VENV_PATH = Path.home() / ".openclaw" / "tools-venv"
sys.path.insert(0, str(VENV_PATH / "lib" / "python3.12" / "site-packages"))

OUTPUT_DIR = Path(__file__).parent.parent / "audio"
OUTPUT_DIR.mkdir(exist_ok=True)

def check_dependencies():
    """Check if required packages are installed"""
    try:
        import torch
        from transformers import pipeline
        print("✓ Dependencies OK")
        return True
    except ImportError as e:
        print(f"✗ Missing dependency: {e}")
        print("Run: pip install transformers torch scipy")
        return False

def generate_narration(text: str, filename: str, voice_preset: str = "v2/de_speaker_0"):
    """Generate narration audio using Bark"""
    try:
        from transformers import AutoProcessor, BarkModel
        import scipy.io.wavfile as wavfile
        import torch
        
        print(f"Generating: {filename}")
        print(f"Text: {text[:50]}...")
        
        # Load model (will be cached after first use)
        processor = AutoProcessor.from_pretrained("suno/bark")
        model = BarkModel.from_pretrained("suno/bark")
        
        # Move to GPU if available
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model = model.to(device)
        
        # Generate audio
        inputs = processor(text, voice_preset=voice_preset)
        inputs = {k: v.to(device) for k, v in inputs.items()}
        
        audio_array = model.generate(**inputs)
        audio_array = audio_array.cpu().numpy().squeeze()
        
        # Save
        output_path = OUTPUT_DIR / f"{filename}.wav"
        wavfile.write(str(output_path), rate=24000, data=audio_array)
        
        print(f"✓ Saved: {output_path}")
        return str(output_path)
        
    except Exception as e:
        print(f"✗ Error generating audio: {e}")
        return None

def generate_simple_tts(text: str, filename: str):
    """Fallback: Use simpler TTS pipeline"""
    try:
        from transformers import pipeline
        import scipy.io.wavfile as wavfile
        
        print(f"Generating (simple TTS): {filename}")
        
        synthesiser = pipeline("text-to-speech", "suno/bark-small")
        speech = synthesiser(text, forward_params={"do_sample": True})
        
        output_path = OUTPUT_DIR / f"{filename}.wav"
        wavfile.write(str(output_path), rate=speech["sampling_rate"], data=speech["audio"])
        
        print(f"✓ Saved: {output_path}")
        return str(output_path)
        
    except Exception as e:
        print(f"✗ Error: {e}")
        return None

# Audio scripts for the simulation
AUDIO_SCRIPTS = {
    "intro": {
        "text": "November 1938. [Pause] Du bist Werner Hoffmann. 35 Jahre alt. Buchhalter. Ein ganz gewöhnlicher Mann... in einer nicht gewöhnlichen Zeit.",
        "type": "narration"
    },
    "sirens_distant": {
        "text": "[Sirenen in der Ferne] [Pause]",
        "type": "effect"
    },
    "glass_breaking": {
        "text": "[Glas zerbricht] [Glas zerbricht]",
        "type": "effect"
    },
    "crowd_murmur": {
        "text": "[Menschen murmeln durcheinander] [Unruhe]",
        "type": "effect"
    },
    "knock_door": {
        "text": "[Klopfen an der Tür] [Pause] [Lautes Klopfen]",
        "type": "effect"
    },
    "chapter1_intro": {
        "text": "Kapitel Eins. Ein gewöhnlicher Abend. [Pause] Das Radio spielt leise Musik. Martha strickt am Fenster. Die Kinder sind längst im Bett.",
        "type": "narration"
    },
    "martha_question": {
        "text": "[Besorgt] Werner? Hörst du das?",
        "type": "dialogue"
    },
    "realization": {
        "text": "[Pause] Du bist jetzt Zeuge. [Pause] Was immer du tust oder nicht tust... du hast gesehen, was hier geschieht.",
        "type": "narration"
    },
    "epilog_passive": {
        "text": "Du hast dich entschieden, nicht hinzusehen. [Seufzen] Es war die sichere Entscheidung. Millionen andere trafen dieselbe Wahl. Und so konnte geschehen... was geschah.",
        "type": "narration"
    },
    "epilog_active": {
        "text": "Du hast versucht, etwas zu tun. In einer Zeit, in der Wegsehen sicherer war... hast du hingesehen. Das änderte nichts am Lauf der Geschichte. Aber vielleicht... an dem, was du im Spiegel sahst.",
        "type": "narration"
    }
}

def generate_all():
    """Generate all audio files"""
    if not check_dependencies():
        return
    
    print(f"\n{'='*50}")
    print("Audio-Generierung für NS-Simulation")
    print(f"{'='*50}\n")
    
    results = {}
    
    for key, data in AUDIO_SCRIPTS.items():
        print(f"\n[{key}]")
        result = generate_simple_tts(data["text"], key)
        results[key] = {
            "file": result,
            "text": data["text"],
            "type": data["type"]
        }
    
    # Save manifest
    manifest_path = OUTPUT_DIR / "manifest.json"
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\n{'='*50}")
    print(f"✓ Manifest saved: {manifest_path}")
    print(f"{'='*50}\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Generate single audio
        text = " ".join(sys.argv[1:])
        generate_simple_tts(text, "custom_output")
    else:
        # Generate all predefined audio
        generate_all()
