#!/usr/bin/env python3
"""
Bildgenerierung für Mammutprojekt via Hugging Face Inference API
Kein lokaler GPU nötig - läuft auf HF-Servern
"""

import requests
import os
from pathlib import Path
import time

# API Setup
API_URL = "https://router.huggingface.co/hf-inference/models/black-forest-labs/FLUX.1-schnell"
HF_TOKEN = os.environ.get("HF_TOKEN") or open(Path.home() / ".openclaw/.env").read().split("HF_TOKEN=")[1].split("\n")[0]
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}

# Output-Verzeichnis
OUTPUT_DIR = Path(__file__).parent.parent / "images" / "generated"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Stil-Präfix
STYLE = "1930s Germany, sepia toned historical photograph, atmospheric, cinematic, "

# Szenen
SCENES = {
    # Werner (Zuschauer)
    "werner_apartment": "modest German apartment interior 1938, wooden furniture, radio, lace curtains, warm evening light",
    "werner_window_flames": "view through window at night, distant orange flames, smoke, German street below, worried observer",
    "werner_street_chaos": "German city street at night 1938, broken glass on cobblestones, smoke, Kristallnacht chaos",
    "werner_helping": "two men in 1930s coats, one helping another into doorway, dark street, secretive, courage",
    "werner_morning_after": "German street morning, broken shop windows, Star of David, glass shards, people looking down",
    
    # David (Opfer)
    "david_school": "Jewish boy outside German school gates 1935, excluded, other children walking past, lonely",
    "david_star": "yellow Star of David being sewn onto coat, hands sewing, 1941, identity mark",
    "david_family": "Jewish family at dinner table 1930s, Shabbat candles, worried faces, intimate moment",
    "david_hiding": "young person in dark cramped attic, fear, light through cracks, hiding 1940s",
    "david_train": "train platform 1941, Jewish families with suitcases, deportation, tragic farewell",
    
    # Allgemein
    "synagogue_fire": "synagogue on fire at night 1938, flames, Kristallnacht, tragic destruction",
    "shop_boycott": "German shop 1933, Star of David painted on window, SA guards, boycott",
}

def query_api(prompt: str) -> bytes:
    """Sende Anfrage an HF Inference API"""
    response = requests.post(
        API_URL,
        headers=HEADERS,
        json={"inputs": prompt}
    )
    
    if response.status_code == 503:
        # Modell wird geladen
        print("    ⏳ Modell wird geladen, warte 20s...")
        time.sleep(20)
        return query_api(prompt)
    
    if response.status_code != 200:
        raise Exception(f"API Error {response.status_code}: {response.text[:200]}")
    
    return response.content

def generate_scene(scene_id: str, prompt: str):
    """Generiere ein Bild"""
    full_prompt = STYLE + prompt
    print(f"  🎨 {scene_id}...")
    
    try:
        image_bytes = query_api(full_prompt)
        output_path = OUTPUT_DIR / f"{scene_id}.png"
        output_path.write_bytes(image_bytes)
        print(f"     ✓ {output_path.name}")
        return True
    except Exception as e:
        print(f"     ✗ Fehler: {e}")
        return False

def main():
    print("=" * 50)
    print("  Mammutprojekt - Bildgenerierung (API)")
    print("=" * 50)
    print(f"  Modell: FLUX.1-schnell")
    print(f"  Output: {OUTPUT_DIR}")
    print("=" * 50)
    
    success = 0
    for scene_id, prompt in SCENES.items():
        if generate_scene(scene_id, prompt):
            success += 1
        time.sleep(2)  # Rate limiting
    
    print(f"\n✓ {success}/{len(SCENES)} Bilder generiert!")

if __name__ == "__main__":
    main()
