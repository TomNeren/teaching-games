---
name: pptx
version: 4.0.0
description: "PowerPoint Skill v4 - Kombiniert pptxgenjs (Von-Scratch) mit python-pptx (Template-basiert, Video-Timer). Für Unterrichtspräsentationen mit integrierten Timern."
license: Proprietary. LICENSE.txt has complete terms
---

# PPTX Skill v4

## Quick Reference

| Task | Methode | Guide |
|------|---------|-------|
| Read/analyze content | python | `python -m markitdown presentation.pptx` |
| Edit or create from template | python-pptx | [editing.md](editing.md) |
| Create from scratch (ohne Video) | pptxgenjs | [pptxgenjs.md](pptxgenjs.md) |
| **Unterricht mit Timer** | python-pptx | [unterricht.md](unterricht.md) ← **NEU** |

---

## Wann welche Methode?

```
┌─────────────────────────────────────────────────────────────┐
│ Braucht die Präsentation Video-Timer?                       │
├──────────────────┬──────────────────────────────────────────┤
│ JA               │ NEIN                                     │
│ → python-pptx    │ → Gibt es eine Vorlage/Template?         │
│   [unterricht.md]│   ├── JA → python-pptx [editing.md]      │
│                  │   └── NEIN → pptxgenjs [pptxgenjs.md]    │
└──────────────────┴──────────────────────────────────────────┘
```

**Warum?** pptxgenjs unterstützt KEINE Video-Einbettung. Für Unterrichtspräsentationen mit Timer ist python-pptx erforderlich.

---

## Reading Content

```bash
# Text extraction
python -m markitdown presentation.pptx

# Visual overview
python scripts/thumbnail.py presentation.pptx

# Raw XML
python scripts/office/unpack.py presentation.pptx unpacked/
```

---

## Unterrichtspräsentation mit Timer (NEU in v4)

**Lies [unterricht.md](unterricht.md) für vollständige Anleitung.**

### Quick-Start

```python
from pptx import Presentation
from pptx.util import Inches

# Vorlage laden
SKILL_PATH = "/mnt/.skills/skills/pptx"
prs = Presentation(f"{SKILL_PATH}/Vorlage.pptx")

# Folie hinzufügen
slide = prs.slides.add_slide(prs.slide_layouts[5])  # Arbeitsphase-Layout

# Timer einfügen (4, 5, 10 min im Skill; Rest extern)
timer_path = f"{SKILL_PATH}/timer/timer_pixel_5min.mp4"
slide.shapes.add_movie(
    timer_path,
    Inches(0), Inches(13.8),    # Position
    Inches(26.67), Inches(1.2), # Größe
    mime_type='video/mp4'
)

prs.save("output.pptx")
```

### Verfügbare Timer

| Im Skill | Extern (Host-Pfad) |
|----------|-------------------|
| 4 min | 3, 6, 7, 8, 9 min |
| 5 min | 12, 15, 20, 25, 30 min |
| 10 min | |

**Externer Pfad:** `/Users/tomren/Library/CloudStorage/GoogleDrive-.../timer_pixel_schnee/`

---

## Von Scratch (ohne Video)

**Lies [pptxgenjs.md](pptxgenjs.md) für vollständige Anleitung.**

```javascript
const pptxgen = require("pptxgenjs");
let pres = new pptxgen();
pres.layout = 'LAYOUT_16x9';

let slide = pres.addSlide();
slide.addText("Hello!", { x: 0.5, y: 0.5, fontSize: 36 });

pres.writeFile({ fileName: "output.pptx" });
```

---

## Template-basiert bearbeiten

**Lies [editing.md](editing.md) für vollständige Anleitung.**

1. `python scripts/office/unpack.py template.pptx unpacked/`
2. XML bearbeiten
3. `python scripts/office/pack.py unpacked/ output.pptx --original template.pptx`

---

## Design Guidelines

### Farbpaletten

| Theme | Primary | Secondary | Accent |
|-------|---------|-----------|--------|
| **Warm Terracotta** | `B85042` | `E7E8D1` | `A7BEAE` |
| **Midnight Executive** | `1E2761` | `CADCFC` | `FFFFFF` |
| **Forest & Moss** | `2C5F2D` | `97BC62` | `F5F5F5` |
| **Teal Trust** | `028090` | `00A896` | `02C39A` |

### Typografie (Unterricht)

| Element | Font | Größe |
|---------|------|-------|
| Haupttitel | Avenir Next Ultra Light | 144pt |
| Folientitel | Avenir Next | 60-72pt |
| Body-Text | Avenir Next | 40-54pt |
| Arbeitsauftrag | Avenir Next | 54-72pt |

---

## QA (Required)

### Content QA

```bash
python -m markitdown output.pptx
python -m markitdown output.pptx | grep -iE "xxxx|lorem|ipsum"
```

### Visual QA

```bash
python scripts/office/soffice.py --headless --convert-to pdf output.pptx
pdftoppm -jpeg -r 150 output.pdf slide
```

---

## Dependencies

```bash
# Python
pip install python-pptx "markitdown[pptx]" Pillow --break-system-packages

# JavaScript
npm install pptxgenjs
```

---

## Changelog

| Version | Datum | Änderungen |
|---------|-------|------------|
| 4.0.0 | 27.01.2026 | Kombiniert pptxgenjs + python-pptx; Video-Timer Support; unterricht.md hinzugefügt |
| 3.0.0 | 27.01.2025 | Wechsel zu pptxgenjs für Von-Scratch |
| 2.0.0 | 24.01.2025 | Template-Workflow mit Keynote-Export |
