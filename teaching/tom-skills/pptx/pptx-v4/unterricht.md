# Unterrichtspräsentationen mit Video-Timer

## Übersicht

Diese Anleitung erklärt wie du Unterrichtspräsentationen mit eingebetteten Video-Timern erstellst. Video-Timer werden mit **python-pptx** eingefügt (pptxgenjs unterstützt keine Videos).

---

## Voraussetzungen

```bash
pip install python-pptx --break-system-packages
```

---

## Keynote-Vorlage

Die Vorlage `Vorlage.pptx` enthält 16 vordefinierte Layouts:

| Index | Name | Verwendung |
|-------|------|------------|
| 0 | Titel | Titelfolie der Stunde |
| 1 | Titel & Foto | Titel mit Vollbild-Hintergrund |
| 2 | Titel & Foto 2 | Titel links, Bild rechts |
| 3 | Titel & Punkte | Agenda, Inhaltsverzeichnis |
| 4 | Titel, Punkte & Foto | Erklärung mit Bild |
| **5** | **Titel, Punkte & Livevideo – klein** | **Arbeitsphase mit Timer** |
| 6 | Titel, Punkte & Livevideo – groß | Arbeitsphase (großer Videobereich) |
| 7 | Abschnitt | These, Statement, Phasenwechsel |
| 8 | Nur Titel | Einfacher Titel |
| 9 | Agenda | Strukturierte Agenda |
| 10 | Aufstellung | Nummerierte Liste |
| 11 | Fakt (groß) | Key Message, Kernaussage |
| 12 | Zitat | Zitat mit Autor |
| 13 | Foto - 3 Stück | Bildergalerie |
| 14 | Foto | Vollbild-Bild |
| 15 | Leer | Freie Gestaltung |

---

## Timer-System

### Im Skill enthalten

| Dauer | Pfad |
|-------|------|
| 4 min | `timer/timer_pixel_4min.mp4` |
| 5 min | `timer/timer_pixel_5min.mp4` |
| 10 min | `timer/timer_pixel_10min.mp4` |

### Extern (auf Host-System)

```
EXTERNAL_PATH = "/Users/tomren/Library/CloudStorage/GoogleDrive-renne.tom@googlemail.com/Meine Ablage/Claude-Meta-Projekt/ppt_update/timer_pixel_schnee/"
```

| Dauer | Dateiname |
|-------|-----------|
| 3 min | `timer_pixel_3min.mp4` |
| 6, 7, 8, 9 min | `timer_pixel_Xmin.mp4` |
| 12, 15, 20, 25, 30 min | `timer_pixel_Xmin.mp4` |

### Timer-Position

- **Y-Position:** 13.8 Zoll vom oberen Rand
- **Breite:** Volle Folienbreite (26.67 Zoll)
- **Höhe:** 1.2 Zoll

---

## Vollständiges Beispiel

```python
#!/usr/bin/env python3
"""Unterrichtspräsentation mit Timer erstellen."""

from pptx import Presentation
from pptx.util import Inches, Pt
import os

# Konfiguration
SKILL_PATH = "/mnt/.skills/skills/pptx"
TEMPLATE_PATH = f"{SKILL_PATH}/Vorlage.pptx"
TIMER_PATH = f"{SKILL_PATH}/timer"
EXTERNAL_TIMER_PATH = "/Users/tomren/Library/CloudStorage/GoogleDrive-renne.tom@googlemail.com/Meine Ablage/Claude-Meta-Projekt/ppt_update/timer_pixel_schnee"

# Timer im Skill
INCLUDED_TIMERS = [4, 5, 10]
AVAILABLE_TIMERS = [3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 20, 25, 30]

# Layouts
LAYOUTS = {
    "titel": 0,
    "titel_foto": 1,
    "titel_punkte": 3,
    "titel_punkte_foto": 4,
    "arbeitsphase": 5,
    "abschnitt": 7,
    "fakt": 11,
    "zitat": 12,
}


def get_timer_path(minutes: int) -> str:
    """Gibt Pfad zum passenden Timer zurück."""
    # Nächst passenden Timer finden
    timer_min = minutes
    if minutes not in AVAILABLE_TIMERS:
        for t in AVAILABLE_TIMERS:
            if t >= minutes:
                timer_min = t
                break
        else:
            timer_min = 30

    filename = f"timer_pixel_{timer_min}min.mp4"

    if timer_min in INCLUDED_TIMERS:
        return f"{TIMER_PATH}/{filename}"
    return f"{EXTERNAL_TIMER_PATH}/{filename}"


def add_timer(slide, minutes: int) -> bool:
    """Fügt Timer-Video am unteren Rand ein."""
    timer_path = get_timer_path(minutes)

    if not os.path.exists(timer_path):
        print(f"⚠️ Timer nicht gefunden: {timer_path}")
        return False

    slide.shapes.add_movie(
        timer_path,
        Inches(0),        # left
        Inches(13.8),     # top
        Inches(26.67),    # width
        Inches(1.2),      # height
        poster_frame_image=None,
        mime_type='video/mp4'
    )
    return True


def set_placeholder(slide, idx: int, text: str):
    """Setzt Text in Placeholder."""
    for shape in slide.placeholders:
        if shape.placeholder_format.idx == idx:
            shape.text = text
            return True
    return False


# Beispiel: Präsentation erstellen
prs = Presentation(TEMPLATE_PATH)

# 1. Titelfolie
slide = prs.slides.add_slide(prs.slide_layouts[LAYOUTS["titel"]])
set_placeholder(slide, 0, "Unterrichtsthema")
set_placeholder(slide, 1, "Untertitel")

# 2. Arbeitsphase mit 5-Minuten-Timer
slide = prs.slides.add_slide(prs.slide_layouts[LAYOUTS["arbeitsphase"]])
set_placeholder(slide, 0, "Think-Pair-Share")
set_placeholder(slide, 1, "Arbeitsauftrag: Analysiere die Quelle...")
add_timer(slide, 5)

# 3. Sicherung mit 10-Minuten-Timer
slide = prs.slides.add_slide(prs.slide_layouts[LAYOUTS["arbeitsphase"]])
set_placeholder(slide, 0, "Gruppenpräsentation")
set_placeholder(slide, 1, "Präsentiert eure Ergebnisse...")
add_timer(slide, 10)

# Speichern
prs.save("unterricht.pptx")
print("✅ Präsentation erstellt")
```

---

## Font-Korrektur

Keynote-Exporte haben manchmal Platzhalter-Fonts:

```python
FONT_REPLACEMENTS = {
    '+mj-lt': 'Avenir Next',
    '+mn-lt': 'Avenir Next',
    '+mj-ea': 'Avenir Next',
    '+mn-ea': 'Avenir Next',
}

def fix_fonts(presentation):
    """Korrigiert Keynote-Platzhalter-Fonts."""
    for slide in presentation.slides:
        for shape in slide.shapes:
            if shape.has_text_frame:
                for para in shape.text_frame.paragraphs:
                    for run in para.runs:
                        if run.font.name in FONT_REPLACEMENTS:
                            run.font.name = FONT_REPLACEMENTS[run.font.name]
    return presentation
```

---

## Layout-Empfehlungen nach Phase

```
EINSTIEG:
├── Bildimpuls       → Layout 4 (Titel, Punkte & Foto)
├── These/Statement  → Layout 7 (Abschnitt)
├── Zitat            → Layout 12 (Zitat)
└── Lernziele        → Layout 3 (Titel & Punkte)

ERARBEITUNG:
├── Arbeitsauftrag   → Layout 5 (Arbeitsphase) + Timer
└── Mit Bild         → Layout 4 + Timer manuell

SICHERUNG:
├── Ergebnisse       → Layout 3 (Titel & Punkte)
├── Key Message      → Layout 11 (Fakt groß)
└── Präsentation     → Layout 5 + Timer

ABSCHLUSS:
├── Fazit            → Layout 7 (Abschnitt)
└── Reflexion        → Layout 3 (Titel & Punkte)
```

---

## Troubleshooting

### Timer nicht gefunden

```
⚠️ Timer nicht gefunden: /Users/tomren/.../timer_pixel_15min.mp4
```

**Lösung:** Prüfe ob der externe Pfad erreichbar ist oder nutze einen im Skill enthaltenen Timer (4, 5, 10 min).

### Fonts werden nicht angezeigt

**Lösung:** `fix_fonts(prs)` vor dem Speichern aufrufen.

### Video spielt nicht ab

**Lösung:** PowerPoint muss Videos im Präsentationsmodus abspielen. In der Bearbeitungsansicht wird nur ein Platzhalter gezeigt.
