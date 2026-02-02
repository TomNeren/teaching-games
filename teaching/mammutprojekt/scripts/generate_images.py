#!/usr/bin/env python3
"""
Bildgenerierung für die NS-Simulation mit Hugging Face
Generiert historische Szenen für die Simulation
"""

import os
import sys
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent.parent / "images"
OUTPUT_DIR.mkdir(exist_ok=True)

# Bilder, die wir brauchen - mit ethisch vertretbaren Prompts
IMAGE_PROMPTS = {
    "living_room_1930s": {
        "prompt": "1930s German middle-class living room interior, warm lighting, radio set, armchair, evening atmosphere, sepia tones, historical photograph style",
        "negative": "modern objects, violence, propaganda",
        "scene": "Prolog - Wohnzimmer"
    },
    "street_night_pogrom": {
        "prompt": "1930s German city street at night, broken shop windows on the ground, distant figures with torches, somber atmosphere, documentary style, black and white",
        "negative": "explicit violence, blood, graphic content, faces in distress",
        "scene": "Kapitel 1 - Die Nacht"
    },
    "window_view_night": {
        "prompt": "View from apartment window at night, 1930s German street below, dim street lights, figures in the distance, noir atmosphere, dramatic shadows",
        "negative": "violence, explicit content",
        "scene": "Kapitel 1 - Blick aus dem Fenster"
    },
    "morning_after_street": {
        "prompt": "1930s German street in early morning, broken glass on sidewalk, closed shutters, empty street, grey overcast sky, melancholy atmosphere, historical photograph",
        "negative": "bodies, blood, explicit violence",
        "scene": "Kapitel 2 - Der Morgen danach"
    },
    "telephone_hallway": {
        "prompt": "1930s German apartment hallway, old rotary telephone on wall table, dim lighting, worried atmosphere, period accurate interior design",
        "negative": "modern objects",
        "scene": "Der Anruf"
    },
    "destroyed_shopfront": {
        "prompt": "1930s destroyed German shop storefront, broken display window, scattered merchandise on street, 'JUDE' graffiti barely visible, documentary photograph style, black and white",
        "negative": "people being hurt, explicit violence, faces",
        "scene": "Das zerstörte Geschäft"
    },
    "neighbor_window": {
        "prompt": "Silhouette of woman and child behind curtained window at night, worried posture, 1930s apartment building, noir lighting",
        "negative": "explicit faces, violence",
        "scene": "Die Rosenthals"
    },
    "office_desk": {
        "prompt": "1930s German office desk with papers, typewriter, portrait of leader on wall (blurred/back), oppressive atmosphere, bureaucratic setting",
        "negative": "explicit Nazi imagery, swastikas clearly visible",
        "scene": "Arbeitsplatz"
    },
    "empty_apartment": {
        "prompt": "Abandoned 1930s apartment interior, furniture covered with sheets, dust particles in light beam, melancholy atmosphere, sense of absence",
        "negative": "violence, people",
        "scene": "Epilog - Verlassene Wohnung"
    },
    "memorial_stolperstein": {
        "prompt": "Brass memorial stone (Stolperstein) embedded in cobblestone street, rain drops, flowers nearby, contemplative mood, close-up perspective",
        "negative": "people, violence",
        "scene": "Epilog - Gedenken"
    }
}

def generate_with_huggingface(prompt: str, negative_prompt: str, filename: str):
    """Generate image using Hugging Face diffusers"""
    try:
        import torch
        from diffusers import StableDiffusionPipeline
        
        print(f"Loading model...")
        
        # Use Stable Diffusion 2.1 (good balance of quality and speed)
        pipe = StableDiffusionPipeline.from_pretrained(
            "stabilityai/stable-diffusion-2-1",
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
        )
        
        if torch.cuda.is_available():
            pipe = pipe.to("cuda")
        
        print(f"Generating: {filename}")
        print(f"Prompt: {prompt[:80]}...")
        
        image = pipe(
            prompt=prompt,
            negative_prompt=negative_prompt,
            num_inference_steps=30,
            guidance_scale=7.5
        ).images[0]
        
        output_path = OUTPUT_DIR / f"{filename}.png"
        image.save(output_path)
        
        print(f"✓ Saved: {output_path}")
        return str(output_path)
        
    except Exception as e:
        print(f"✗ Error: {e}")
        return None

def generate_with_api(prompt: str, filename: str):
    """Generate image using Hugging Face Inference API (no local GPU needed)"""
    import requests
    
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
    
    # Check for HF token
    hf_token = os.environ.get("HF_TOKEN") or os.environ.get("HUGGINGFACE_TOKEN")
    
    headers = {}
    if hf_token:
        headers["Authorization"] = f"Bearer {hf_token}"
    
    print(f"Generating via API: {filename}")
    
    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json={"inputs": prompt},
            timeout=120
        )
        
        if response.status_code == 200:
            output_path = OUTPUT_DIR / f"{filename}.png"
            with open(output_path, "wb") as f:
                f.write(response.content)
            print(f"✓ Saved: {output_path}")
            return str(output_path)
        else:
            print(f"✗ API Error: {response.status_code} - {response.text[:200]}")
            return None
            
    except Exception as e:
        print(f"✗ Error: {e}")
        return None

def generate_placeholder(filename: str, description: str):
    """Generate a placeholder SVG image"""
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="400" viewBox="0 0 800 400">
    <rect width="800" height="400" fill="#2a2a2a"/>
    <text x="400" y="180" font-family="Georgia" font-size="20" fill="#888" text-anchor="middle">[Bild wird generiert]</text>
    <text x="400" y="220" font-family="Georgia" font-size="16" fill="#666" text-anchor="middle">{description}</text>
</svg>'''
    
    output_path = OUTPUT_DIR / f"{filename}.svg"
    with open(output_path, "w") as f:
        f.write(svg_content)
    
    print(f"✓ Placeholder: {output_path}")
    return str(output_path)

def generate_all(use_api=True):
    """Generate all images"""
    print(f"\n{'='*50}")
    print("Bildgenerierung für NS-Simulation")
    print(f"{'='*50}\n")
    
    results = {}
    
    for key, data in IMAGE_PROMPTS.items():
        print(f"\n[{key}] - {data['scene']}")
        
        if use_api:
            result = generate_with_api(data["prompt"], key)
        else:
            result = generate_with_huggingface(
                data["prompt"], 
                data.get("negative", ""),
                key
            )
        
        if not result:
            # Fallback to placeholder
            result = generate_placeholder(key, data["scene"])
        
        results[key] = {
            "file": result,
            "prompt": data["prompt"],
            "scene": data["scene"]
        }
    
    # Save manifest
    import json
    manifest_path = OUTPUT_DIR / "manifest.json"
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\n{'='*50}")
    print(f"✓ Manifest saved: {manifest_path}")
    print(f"{'='*50}\n")

if __name__ == "__main__":
    # Default: generate placeholders (safe, fast)
    # Use --api flag to use Hugging Face API
    # Use --local flag to use local diffusers
    
    if "--api" in sys.argv:
        generate_all(use_api=True)
    elif "--local" in sys.argv:
        generate_all(use_api=False)
    else:
        print("Generating placeholder images...")
        for key, data in IMAGE_PROMPTS.items():
            generate_placeholder(key, data["scene"])
        print("\n✓ Placeholders created. Run with --api or --local for real images.")
