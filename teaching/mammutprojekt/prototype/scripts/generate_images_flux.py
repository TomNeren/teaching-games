#!/usr/bin/env python3
"""
Bildgenerierung für Mammutprojekt mit FLUX.1-schnell
Historische Szenen der NS-Zeit, 1935-1941
"""

import torch
from diffusers import FluxPipeline
from pathlib import Path
import json

# Output-Verzeichnis
OUTPUT_DIR = Path(__file__).parent.parent / "images" / "generated"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Stil-Präfix für konsistente historische Ästhetik
STYLE_PREFIX = "1930s Germany, sepia toned photograph style, historical, atmospheric, cinematic lighting, "

# Szenen-Definitionen
SCENES = {
    # === WERNER (Zuschauer) ===
    "werner_apartment": {
        "prompt": "modest German apartment interior 1938, wooden furniture, radio on table, lace curtains, warm evening light through window, cozy middle-class home",
        "negative": "modern, bright colors, luxury"
    },
    "werner_window_flames": {
        "prompt": "view through apartment window at night, distant orange glow of fires, smoke rising, German city street below, person looking out worried, November 1938",
        "negative": "daylight, happy, modern"
    },
    "werner_street_chaos": {
        "prompt": "German city street at night 1938, broken glass on cobblestones, smoke, people running, shopfronts damaged, chaos, Kristallnacht",
        "negative": "peaceful, modern, daylight"
    },
    "werner_helping_neighbor": {
        "prompt": "two men in 1930s clothing, one helping another into doorway, dark street, secretive, dangerous atmosphere, act of courage",
        "negative": "bright, happy, modern"
    },
    "werner_morning_after": {
        "prompt": "German street morning after Kristallnacht, broken shop windows with Star of David, glass shards, smoke damage, people walking past looking down, shame",
        "negative": "pristine, modern, happy"
    },
    
    # === DAVID (Opfer) ===
    "david_school_rejection": {
        "prompt": "Jewish boy standing outside German school gates 1935, other children walking in, excluded, lonely, autumn, rejection",
        "negative": "happy, included, modern"
    },
    "david_yellow_star": {
        "prompt": "close-up of yellow Star of David being sewn onto coat, 1941 Germany, hands sewing, shame, identity mark",
        "negative": "pride, modern, bright"
    },
    "david_family_dinner": {
        "prompt": "Jewish family sitting around modest dinner table 1930s Germany, Shabbat candles, worried faces, father reading, intimate family moment under threat",
        "negative": "wealthy, happy, carefree"
    },
    "david_hiding": {
        "prompt": "young person hiding in dark cellar or attic, 1940s, fear, cramped space, light through cracks, hiding from persecution",
        "negative": "open, safe, bright"
    },
    "david_deportation_train": {
        "prompt": "crowded train platform 1941, Jewish families with suitcases, German soldiers, deportation scene, tragic farewell, grey atmosphere",
        "negative": "vacation, happy, modern"
    },
    
    # === ALLGEMEIN ===
    "synagogue_burning": {
        "prompt": "synagogue building on fire at night 1938, flames rising, crowd watching, Kristallnacht, tragic destruction of sacred place",
        "negative": "peaceful, modern, daylight"
    },
    "jewish_shop_boycott": {
        "prompt": "German shop 1933 with Star of David and 'Jude' painted on window, SA guards blocking entrance, boycott sign, intimidation",
        "negative": "normal shopping, modern"
    },
    "nuremberg_rally": {
        "prompt": "Nazi rally 1930s, massive flags, organized crowd, propaganda, ominous atmosphere, Nuremberg style, historical",
        "negative": "modern, peaceful protest"
    }
}

def load_pipeline():
    """Lade FLUX.1-schnell Pipeline"""
    print("🎨 Lade FLUX.1-schnell...")
    pipe = FluxPipeline.from_pretrained(
        "black-forest-labs/FLUX.1-schnell",
        torch_dtype=torch.bfloat16
    )
    pipe.enable_model_cpu_offload()  # Spart VRAM
    return pipe

def generate_image(pipe, scene_id: str, scene_data: dict):
    """Generiere ein Bild für eine Szene"""
    prompt = STYLE_PREFIX + scene_data["prompt"]
    
    print(f"  Generiere: {scene_id}")
    
    image = pipe(
        prompt=prompt,
        guidance_scale=0.0,  # FLUX.1-schnell braucht keine guidance
        num_inference_steps=4,  # Schnell!
        max_sequence_length=256,
        generator=torch.Generator("cpu").manual_seed(42)  # Reproduzierbar
    ).images[0]
    
    output_path = OUTPUT_DIR / f"{scene_id}.png"
    image.save(output_path)
    print(f"  ✓ Gespeichert: {output_path}")
    return output_path

def main():
    print("=" * 50)
    print("  Mammutprojekt - Bildgenerierung")
    print("=" * 50)
    
    pipe = load_pipeline()
    
    generated = []
    for scene_id, scene_data in SCENES.items():
        try:
            path = generate_image(pipe, scene_id, scene_data)
            generated.append({"id": scene_id, "path": str(path)})
        except Exception as e:
            print(f"  ✗ Fehler bei {scene_id}: {e}")
    
    # Manifest speichern
    manifest_path = OUTPUT_DIR / "manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(generated, f, indent=2)
    
    print(f"\n✓ {len(generated)} Bilder generiert!")
    print(f"  Manifest: {manifest_path}")

if __name__ == "__main__":
    main()
