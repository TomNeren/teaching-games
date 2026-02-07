---
name: unterrichts-medien
description: Erstellt Bilder, Grafiken, Infografiken und einfache Visualisierungen für Unterrichtsmaterialien mittels ComfyUI (lokal) oder Fallback-Optionen. Nutze bei Anfragen nach Bildmaterial, Illustrationen, Charts, Infografiken oder visuellen Materialien für den Unterricht.
---

# Unterrichts-Medien Skill

Erstellt visuelle Unterrichtsmaterialien über ComfyUI (lokal bevorzugt) oder Fallback-Systeme.

## When to Use This Skill

**Trigger-Wörter:**
- "Bild erstellen", "Grafik", "Illustration"
- "Infografik", "Chart", "Diagramm"
- "Bildimpuls", "Visual", "Poster"
- "Bildkarten", "Flashcards"
- Handover enthält Bild-Prompts oder Bildanforderungen

**Nicht verwenden für:**
- Komplexe Datenvisualisierungen (nutze Excel/Charts)
- Fotografien mit echten Personen
- Urheberrechtlich geschützte Charaktere

---

## Verfügbare Tools (Prioritätsreihenfolge)

### 🥇 ComfyUI (LOKAL - PRIMÄR)

**Setup:**
- Lokale Installation: `~/ComfyUI`
- Modell: FLUX.1-schnell (GGUF Q4_0, ~6.4 GB)
- Läuft auf: `http://127.0.0.1:8188`
- MCP Server: `comfy-ui-mcp-server`

**Tool-Name:** `comfyui:generate_image`

**Vorteile:**
- ✅ Schnell & kostenlos
- ✅ Offline verfügbar
- ✅ Hohe Qualität (FLUX.1-schnell)
- ✅ Volle Kontrolle
- ✅ Keine API-Limits
- ✅ Apache 2.0 Lizenz (kommerziell nutzbar)

**Verwendung:**
```json
{
  "prompt": "[Dein FLUX-optimierter Prompt]",
  "width": 1024,
  "height": 1024,
  "seed": -1
}
```

**Start ComfyUI:**
```bash
cd ~/ComfyUI
source venv/bin/activate
python main.py --use-pytorch-cross-attention --force-fp16
```

### 🥈 Nanobanana (Google Gemini - BACKUP)

**Tool-Name:** `nanobanana:generate_image`

**Parameter:**
- `prompt`: Bildbeschreibung
- `aspect_ratio`: "1:1", "16:9", "3:4", etc.
- `model`: "pro" oder "normal"
- `output_path`: Absoluter Pfad zum Speichern

**Verwendung:**
```python
nanobanana:generate_image(
    prompt="[Prompt]",
    aspect_ratio="16:9",
    model="pro",
    output_path="/absolute/path/to/image.png"
)
```

### 🥉 Hugging Face Spaces (FALLBACK)

**1. FLUX.1 Kontext (Bearbeitung)**
```
Tool: gr1_flux_1_kontext_dev_infer
Parameter:
- prompt, input_image, guidance_scale: 2.5, steps: 28
```

**2. Z-Image Turbo (Schnell)**
```
Tool: gr4_z_image_turbo_generate
Parameter:
- prompt, resolution: "1024x1024", steps: 4-8
```

---

## FLUX Prompting Best Practices (Black Forest Labs)

### Grund-Struktur:
```
Subject → Action → Environment → Lighting → Style/Modifiers
```

### ✅ Do's:
- **Natürliche Sprache** verwenden (40-50 Wörter optimal)
- **Konkrete Aktionen** beschreiben: "running", "sitting", "celebrating"
- **Beleuchtung spezifizieren**: "golden hour lighting", "studio lighting"
- **Foto-Parameter** für Realismus: "f/8 sharp focus", "85mm lens"
- **Text in Anführungszeichen**: `"The text 'OPEN' in red letters"`

### ❌ Don'ts:
- **KEINE Quality Tags**: "masterpiece", "best quality", "highly detailed" (unnötig!)
- **KEINE Künstlernamen**: FLUX kennt keine spezifischen Künstler (EU-Recht)
- Stattdessen: **Stil-Beschreibungen** wie "Van Gogh painting style with swirling brushstrokes"
- **Keine Keyword-Listen**: Vermeide zufällige Aneinanderreihung

---

## Prompt-Templates für Unterrichtsmaterialien (FLUX-optimiert)

### Kindgerechte Illustrationen
```
[MOTIV] [AKTION/SITUATION], photorealistic style,
bright cheerful colors with high contrast, simple clean composition,
educational material, f/8 sharp focus
```

**Beispiel:**
```
Children playing in a park during autumn, photorealistic style,
bright cheerful colors with high contrast, simple clean composition,
educational material, f/8 sharp focus
```

### Infografiken
```
[THEMA] infographic, educational diagram with simple icons,
pastel colors with clear visual hierarchy, minimalist design,
high contrast, f/8 sharp focus
```

**Beispiel:**
```
Water cycle infographic, educational diagram with simple icons,
pastel colors with clear visual hierarchy, minimalist design,
high contrast, f/8 sharp focus
```

### Länderflaggen & Kulturbilder
```
[LAND] cultural scene with children [AKTION], [SPEZIFISCHES ELEMENT],
photorealistic style, diverse representation,
cheerful atmosphere with bright colors, f/8 sharp focus
```

**Beispiel:**
```
British cultural scene with children celebrating at a fancy dress party, colorful costumes and decorations,
photorealistic style, diverse representation,
cheerful atmosphere with bright colors, f/8 sharp focus
```

### Emotionen/Situationen (für Sprachunterricht)
```
[PERSON/TIER] showing [EMOTION], photorealistic style,
expressive face with clear emotion, solid color background,
educational flashcard, f/8 sharp focus
```

**Beispiel:**
```
Young child showing happiness, photorealistic style,
expressive face with clear emotion, solid color background,
educational flashcard, f/8 sharp focus
```

### Bastelmaterial-Illustrationen
```
[GEGENSTAND] [SCHRITT-BESCHREIBUNG], step-by-step craft instruction,
simple line drawing with numbered steps, clear visual guide,
educational worksheet style, high contrast, f/8 sharp focus
```

**Beispiel:**
```
Paper shaker being assembled with rice inside, step-by-step craft instruction,
simple line drawing with numbered steps, clear visual guide,
educational worksheet style, high contrast, f/8 sharp focus
```

---

## Workflow für Bildgenerierung

### Schritt 1: Anforderung analysieren
- Was zeigt das Bild?
- Für welche Altersgruppe?
- Beamer-Projektion oder Arbeitsblatt?
- Farbig oder schwarz-weiß?

### Schritt 2: Tool-Auswahl
1. **ComfyUI verfügbar?** → Nutze ComfyUI (lokal, schnell, kostenlos, ERSTE WAHL)
2. Nicht verfügbar? → **Nanobanana** (Google Gemini)
3. Beides nicht verfügbar? → **Hugging Face** Spaces

### Schritt 3: Prompt formulieren
- Nutze FLUX-optimiertes Template von oben
- Ergänze spezifische Details
- Füge Beleuchtung hinzu wenn relevant
- Struktur: Subject → Action → Style → Technical

### Schritt 4: ComfyUI Generierung
```bash
# 1. ComfyUI starten (falls nicht läuft)
cd ~/ComfyUI && source venv/bin/activate
python main.py --use-pytorch-cross-attention --force-fp16

# 2. Tool aufrufen
comfyui:generate_image(
    prompt="[FLUX-optimierter Prompt]",
    width=1024,
    height=1024,
    seed=-1  # oder fester Seed für Reproduzierbarkeit
)
```

### Schritt 5: Speichern
```
/mnt/user-data/outputs/[Klasse]/[Einheit]/[Stunde]_IMG_[Titel].png
```

---

## FLUX.1-schnell Spezifika

### Modell-Eigenschaften:
- **Steps:** 1-4 optimal (sehr schnell!)
- **Lizenz:** Apache 2.0 (kommerziell nutzbar)
- **Stärken:** Schnelle Generierung bei guter Qualität
- **Fotografie-Parameter:**
  - `f/1.4` = unscharfer Hintergrund (Bokeh)
  - `f/8` = alles scharf (empfohlen für Bildungsmaterialien)
  - `85mm lens` = Portrait
  - `24mm` = Weitwinkel

### Text in Bildern:
```
"The text 'VOCABULARY' appears in bold letters at the top",
centered, elegant sans-serif typography
```

---

## Qualitätsrichtlinien

### Do's ✓
- Einfache, klare Kompositionen
- Helle, freundliche Farben
- Hoher Kontrast für Beamer (`high contrast`)
- Kindgerechte Darstellungen
- Diversität bei Personen
- Konsistenter Stil innerhalb einer Einheit (gleicher Seed)
- FLUX-Struktur: Subject → Action → Style

### Don'ts ✗
- Keine echten Personen/Fotos-Referenzen
- Keine urheberrechtlich geschützten Charaktere
- Keine Künstlernamen (stattdessen Stil-Beschreibungen)
- Keine Quality Tags ("masterpiece", "best quality")
- Kein Text im Bild ohne Anführungszeichen
- Keine zu komplexen Szenen
- Keine gruseligen/beängstigenden Elemente
- Keine stereotypen Darstellungen

---

## Beispiel-Workflows

### Beispiel 1: Bildimpuls "UK Carnival"
```python
# ComfyUI (ERSTE WAHL)
comfyui:generate_image(
    prompt="""British children celebrating at a fancy dress party,
    wearing colorful pirate and princess costumes,
    indoor party setting with balloons and streamers,
    photorealistic style, cheerful atmosphere with bright colors,
    f/8 sharp focus""",
    width=1024,
    height=1024,
    seed=-1
)
```

### Beispiel 2: Emotionskarte "Happy"
```python
comfyui:generate_image(
    prompt="""Young child showing happiness with wide smile,
    photorealistic style, expressive face with clear emotion,
    solid yellow background, educational flashcard, f/8 sharp focus""",
    width=1024,
    height=1024,
    seed=12345  # Fester Seed für Serie
)
```

### Beispiel 3: Infografik "Water Cycle"
```python
comfyui:generate_image(
    prompt="""Water cycle infographic showing evaporation condensation precipitation,
    educational diagram with simple icons and arrows,
    pastel blue colors with clear visual hierarchy,
    minimalist design, high contrast, f/8 sharp focus""",
    width=1024,
    height=768,
    seed=-1
)
```

---

## Integration mit anderen Skills

### Mit arbeitsblatt-erstellen:
1. Bild mit ComfyUI generieren
2. Bild in `/mnt/user-data/outputs/` speichern
3. Im Arbeitsblatt referenzieren: "Siehe Bild 1.1"
4. Bild separat ausdrucken oder digital zeigen

### Mit unterrichtsstunde-erstellen:
1. Bilder für Bildimpulse mit ComfyUI generieren
2. In PowerPoint als Folien einfügen
3. Dateinamen notieren für Referenz

---

## Fehlerbehebung

### Problem: ComfyUI nicht verfügbar
**Lösung:**
```bash
cd ~/ComfyUI
source venv/bin/activate
python main.py --use-pytorch-cross-attention --force-fp16
```
Dann Claude Desktop neu starten (Cmd+Q)

### Problem: Bild hat unerwünschten Text
**Lösung:** Füge "no text in image, no words, no letters" zum Prompt hinzu

### Problem: Bild zu komplex
**Lösung:** Reduziere Elemente im Prompt, nutze "simple composition, minimalist"

### Problem: Farben zu dunkel für Beamer
**Lösung:** Füge "bright colors, high contrast, f/8 sharp focus" hinzu

### Problem: Stil inkonsistent zwischen Bildern
**Lösung:** Nutze identischen Stil-Suffix für alle Bilder einer Serie, verwende **gleichen Seed**

### Problem: Qualität nicht gut genug
**Lösung:** KEINE Quality Tags hinzufügen! Stattdessen:
- Konkretere Beschreibung
- Beleuchtung spezifizieren
- Foto-Parameter ergänzen (`f/8`, `85mm lens`)

---

## Checkliste für Bildgenerierung

- [ ] ComfyUI läuft (http://127.0.0.1:8188)
- [ ] Prompt folgt FLUX-Struktur: Subject → Action → Style
- [ ] KEINE Quality Tags verwendet
- [ ] KEINE Künstlernamen verwendet
- [ ] Stil ist altersgerecht
- [ ] Keine urheberrechtlichen Probleme
- [ ] Hoher Kontrast für Projektion (`f/8 sharp focus`)
- [ ] Dateiname folgt Konvention
- [ ] Bild im korrekten Ordner gespeichert
- [ ] Referenz in Material (AB/PPT) eingetragen

---

## Quick Reference

**ComfyUI starten:**
```bash
cd ~/ComfyUI && source venv/bin/activate && python main.py --use-pytorch-cross-attention --force-fp16
```

**Basis-Prompt-Struktur:**
```
[Subject] [Action], [Style], [Details], [Lighting], [Technical: f/8 sharp focus]
```

**Typische Werte:**
- Width/Height: 1024x1024 (Standard), 1024x768 (Querformat)
- Seed: -1 (random) oder fester Wert (reproduzierbar)
- Steps: 1-4 (FLUX.1-schnell optimal)

---

*Version: 2.0 - FLUX-optimiert*
*Erstellt: Januar 2026*
*Abhängigkeit: ComfyUI (primär), Nanobanana/Hugging Face (Fallback)*
*Modell: FLUX.1-schnell (Black Forest Labs)*
