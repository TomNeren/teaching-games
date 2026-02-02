#!/usr/bin/env python3
"""
Musik-Generierung für Mammutprojekt via Hugging Face Inference API
Klassische Instrumente, atmosphärische Soundtracks
"""

import requests
import os
from pathlib import Path
import time

# API Setup
API_URL = "https://router.huggingface.co/hf-inference/models/facebook/musicgen-small"
HF_TOKEN = os.environ.get("HF_TOKEN") or open(Path.home() / ".openclaw/.env").read().split("HF_TOKEN=")[1].split("\n")[0]
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}

# Output-Verzeichnis
OUTPUT_DIR = Path(__file__).parent.parent / "audio" / "music"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Musik-Tracks nach Stimmung
TRACKS = {
    # Friedlich / Hoffnung
    "peaceful_home": "gentle piano and violin, warm domestic 1930s atmosphere, nostalgic, soft",
    "hope_theme": "hopeful orchestral strings, cello melody, tender, emotional, classical",
    "innocence": "light playful piano, innocent melody, gentle flute, nostalgic, bittersweet",
    
    # Spannung / Bedrohung  
    "tension": "dark orchestral, low strings tremolo, ominous, suspenseful, building dread",
    "danger": "urgent strings, dramatic timpani, threatening brass, dark classical",
    "hiding": "quiet tense strings, heartbeat rhythm, fearful, minimal classical, suspense",
    
    # Trauer / Verlust
    "grief": "sorrowful violin solo, mourning cello, slow tempo, devastating loss, classical",
    "farewell": "melancholic piano, tearful strings, separation, bittersweet, emotional",
    "aftermath": "sparse piano notes, silence between, devastation, hollow, minimal",
    
    # Chaos / Gewalt
    "chaos": "chaotic orchestral, dissonant strings, violent brass, terrifying, dramatic",
    "mob": "aggressive percussion, threatening brass fanfare, ominous march",
    
    # Mut / Widerstand
    "courage": "brave orchestral theme, determined strings, quiet heroism, hopeful",
    "kindness": "gentle hopeful piano, warm strings, humanity, tender moment",
    
    # Reflexion
    "guilt": "contemplative piano, regretful cello, moral weight, slow, introspective",
    "remember": "solemn orchestral, memorial, dignified strings, classical requiem"
}

def query_api(prompt: str) -> bytes:
    """Sende Anfrage an HF Inference API"""
    response = requests.post(
        API_URL,
        headers=HEADERS,
        json={"inputs": prompt}
    )
    
    if response.status_code == 503:
        print("    ⏳ Modell wird geladen, warte 30s...")
        time.sleep(30)
        return query_api(prompt)
    
    if response.status_code != 200:
        raise Exception(f"API Error {response.status_code}: {response.text[:200]}")
    
    return response.content

def generate_track(track_id: str, prompt: str):
    """Generiere einen Musik-Track"""
    print(f"  🎵 {track_id}...")
    
    try:
        audio_bytes = query_api(prompt)
        output_path = OUTPUT_DIR / f"{track_id}.flac"
        output_path.write_bytes(audio_bytes)
        print(f"     ✓ {output_path.name}")
        return True
    except Exception as e:
        print(f"     ✗ Fehler: {e}")
        return False

def main():
    print("=" * 50)
    print("  Mammutprojekt - Musik-Generierung (API)")
    print("=" * 50)
    print(f"  Modell: MusicGen-Small")
    print(f"  Output: {OUTPUT_DIR}")
    print("=" * 50)
    
    success = 0
    for track_id, prompt in TRACKS.items():
        if generate_track(track_id, prompt):
            success += 1
        time.sleep(3)  # Rate limiting
    
    print(f"\n✓ {success}/{len(TRACKS)} Tracks generiert!")
    
    # Übersicht
    print("\n📋 Verwendung im Spiel:")
    print("-" * 40)
    print("  Friedlich: peaceful_home, hope_theme, innocence")
    print("  Spannung:  tension, danger, hiding")
    print("  Trauer:    grief, farewell, aftermath")
    print("  Chaos:     chaos, mob")
    print("  Mut:       courage, kindness")
    print("  Reflexion: guilt, remember")

if __name__ == "__main__":
    main()
