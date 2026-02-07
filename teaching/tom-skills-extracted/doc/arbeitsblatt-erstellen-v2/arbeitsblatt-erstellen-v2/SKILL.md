---
name: arbeitsblatt-erstellen-v2
description: Erstellt Arbeitsblätter und Klassenarbeiten im .docx-Format aus Unterrichtsplanungen. Verwendet bereinigte Vorlagen mit konsistenten Platzhaltern. NUR nach abgeschlossener Stundenplanung verwenden.
---

# Skill: Arbeitsblatt erstellen (v2)

**Version:** 2.0.0
**Stand:** 24.01.2025
**Trigger:** "erstelle Arbeitsblatt", "erstelle Klassenarbeit", "AB erstellen", "Worksheet erstellen"

---

## Zweck

Erstellt professionelle Arbeitsblätter und Klassenarbeiten im Word-Format (.docx) basierend auf einer Stundenplanung. Verwendet Toms Design-System mit einheitlichem Header und Logo.

---

## Voraussetzungen

- Vollständige Stundenplanung aus Phase 2A/2B des `unterrichtsplanung-workflow` Skills
- Oder: Handover-Dokument mit Lernzielen, Aufgaben und Differenzierung

---

## Dateien in diesem Skill

```
/mnt/skills/user/arbeitsblatt-erstellen-v2/
├── SKILL.md                           ← Diese Datei
├── templates/
│   ├── Vorlage_Fach.docx             ← Normale Arbeitsblätter
│   └── Vorlage_Klassenarbeit.docx    ← Tests/Klassenarbeiten
└── scripts/
    └── create_worksheet.py           ← Automatisierte Erstellung
```

---

## Design-System

### Header-Struktur (beide Vorlagen)

```
┌─────────────────────────────────┬─────────────┬──────────────┐
│ Arbeitsblatt / Klassenarbeit    │   [LOGO]    │              │
│ [Thema]                         │             │              │
├─────────────────────────────────┼─────────────┼──────────────┤
│ Lernziele: / Punkte:            │   [Fach]    │ Niveau:      │
│ [Ziel 1]                        │             │ [A / B / C]  │
│ [Ziel 2]                        │             │              │
│ [Ziel 3]                        │             │              │
├─────────────────────────────────┼─────────────┴──────────────┤
│ Name:            Vorname:       │ Datum:                     │
└─────────────────────────────────┴────────────────────────────┘
```

### Typografie

| Element | Schriftart | Größe | Hinweis |
|---------|------------|-------|---------|
| Header | Avenir Next | Aus Vorlage | Logo, Fach, Niveau |
| Normal | Avenir Next | 11pt | Body-Text, Listen |
| Heading 1 | Avenir Next Ultra Light | 16pt | Hauptüberschriften, unterstrichen |
| Heading 2 | Avenir Next Medium | 13pt | Unterüberschriften, unterstrichen |

---

## Vorlagen-Übersicht

### Vorlage_Fach.docx (Normale Arbeitsblätter)

| Platzhalter | Beschreibung | Beispiel | Max. Länge |
|-------------|--------------|----------|------------|
| `[Thema]` | Titel des Arbeitsblatts | "Passive Voice" | ~50 Zeichen |
| `[Fach]` | Unterrichtsfach | "Englisch", "LWK", "GGK" | ~15 Zeichen |
| `[Ziel 1 – nicht länger als eine Zeile]` | Lernziel 1 | "I can identify passive voice" | ~60 Zeichen |
| `[Ziel 2 – nicht länger als eine Zeile]` | Lernziel 2 | "I can transform sentences" | ~60 Zeichen |
| `[Ziel 3 – nicht länger als eine Zeile]` | Lernziel 3 | "I can use passive in writing" | ~60 Zeichen |
| `[A / B / C]` | Niveau (NUR ein Buchstabe!) | "B" | 1 Zeichen |

### Vorlage_Klassenarbeit.docx (Tests)

| Platzhalter | Beschreibung | Beispiel |
|-------------|--------------|----------|
| `Klassenarbeit [1/2/3/4]` | Nummer ersetzen | "Klassenarbeit 2" |
| `[Thema]` | Titel der Arbeit | "Unit 3: Travel" |
| `[Fach]` | Unterrichtsfach | "Englisch" |
| `[abhängig von Aufbau]` | Maximale Punktzahl | "45" |
| `[A / B / C]` | Niveau | "B" |

---

## Erstellungs-Strategie

### Konzept: Header ersetzen, Body komplett neu

Die Vorlagen enthalten **Beispiel-Inhalte** im Body-Bereich. Diese werden **vollständig entfernt und durch neuen Inhalt ersetzt**.

```
VORHER (Vorlage):
├── Header (Tabelle) → Platzhalter ersetzen
└── Body             → Beispieltext "Erarbeitungsphase 1..."

NACHHER (Fertiges AB):
├── Header (Tabelle) → Mit echten Werten gefüllt
└── Body             → Komplett neuer Inhalt aus Planung
```

---

## KRITISCHE REGELN

### 1. ENCODING (Umlaute)

```
✅ RICHTIG: ä, ö, ü, ß, Ä, Ö, Ü
❌ FALSCH:  ae, oe, ue, ss, Ae, Oe, Ue

NIEMALS ae/oe/ue verwenden! Immer echte Umlaute!
```

### 2. Platzhalter VOLLSTÄNDIG ersetzen

Nach Erstellung darf KEIN `[...]` mehr im Header sein!

### 3. Niveau: NUR EIN Buchstabe

```
✅ RICHTIG: "B"
❌ FALSCH:  "A / B / C" oder "Niveau B"
```

### 4. IMMER den public docx-Skill zuerst lesen

```bash
view /mnt/skills/public/docx/SKILL.md
```

---

## Python-Script Nutzung

### Basis-Pfade

```python
SKILL_PATH = "/mnt/skills/user/arbeitsblatt-erstellen-v2"
TEMPLATE_AB = f"{SKILL_PATH}/templates/Vorlage_Fach.docx"
TEMPLATE_KA = f"{SKILL_PATH}/templates/Vorlage_Klassenarbeit.docx"
```

### Komplettes Beispiel (Arbeitsblatt)

```python
from docx import Document
from pathlib import Path

# === CONFIGURATION ===
SKILL_PATH = Path("/mnt/skills/user/arbeitsblatt-erstellen-v2")
TEMPLATE_AB = SKILL_PATH / "templates" / "Vorlage_Fach.docx"

# === 1. VORLAGE LADEN ===
doc = Document(str(TEMPLATE_AB))

# === 2. HEADER-PLATZHALTER ERSETZEN ===
replacements = {
    '[Thema]': 'Passive Voice – Introduction',
    '[Fach]': 'Englisch',
    '[Ziel 1 – nicht länger als eine Zeile]': 'I can identify passive voice',
    '[Ziel 2 – nicht länger als eine Zeile]': 'I can explain when to use it',
    '[Ziel 3 – nicht länger als eine Zeile]': 'I can transform sentences',
    '[A / B / C]': 'B',
}

for table in doc.tables:
    for row in table.rows:
        for cell in row.cells:
            for paragraph in cell.paragraphs:
                full_text = "".join(run.text for run in paragraph.runs)
                for old, new in replacements.items():
                    if old in full_text:
                        full_text = full_text.replace(old, new)
                if paragraph.runs:
                    paragraph.runs[0].text = full_text
                    for run in paragraph.runs[1:]:
                        run.text = ""

# === 3. BODY LÖSCHEN UND NEU SCHREIBEN ===
# Alle Paragraphen nach dem ersten entfernen
while len(doc.paragraphs) > 1:
    p = doc.paragraphs[-1]._element
    p.getparent().remove(p)
if doc.paragraphs:
    doc.paragraphs[0].clear()

# Neuen Inhalt einfügen (nutzt Document Styles!)
from docx.shared import Inches

# Überschrift - nutzt Heading 1 Style (Avenir Next Ultra Light, 16pt)
p = doc.add_paragraph("Part 1: Understanding Passive Voice", style='Heading 1')
p.runs[0].underline = True  # Style-Underline muss explizit gesetzt werden

# Task-Überschrift - nutzt Heading 2 Style (Avenir Next Medium, 13pt)
p = doc.add_paragraph("Task 1: Identify the passive", style='Heading 2')
p.runs[0].underline = True

# Anweisung - nutzt Normal Style (Avenir Next)
p = doc.add_paragraph("Read the sentences. Underline the passive constructions.")

# Nummerierte Aufgaben
for i, sentence in enumerate([
    "The book was written by J.K. Rowling.",
    "English is spoken in many countries.",
], 1):
    p = doc.add_paragraph(f"({i}) {sentence}")
    p.paragraph_format.left_indent = Inches(0.5)

# === 4. SPEICHERN ===
output_path = "/mnt/user-data/outputs/AB_01_PassiveVoice_NiveauB.docx"
doc.save(output_path)
print(f"✅ Gespeichert: {output_path}")
```

### Komplettes Beispiel (Klassenarbeit)

```python
from docx import Document
from pathlib import Path

SKILL_PATH = Path("/mnt/skills/user/arbeitsblatt-erstellen-v2")
TEMPLATE_KA = SKILL_PATH / "templates" / "Vorlage_Klassenarbeit.docx"

doc = Document(str(TEMPLATE_KA))

# Klassenarbeit-spezifische Platzhalter
replacements = {
    '[Thema]': 'Unit 3: Travel and Tourism',
    '[Fach]': 'Englisch',
    'Klassenarbeit [1/2/3/4]': 'Klassenarbeit 2',
    '[abhängig von Aufbau]': '45',
    '[A / B / C]': 'B',
}

# ... (gleiche Ersetzungs- und Body-Logik wie oben)
```

---

## Validierung (PFLICHT!)

```python
import re
from docx import Document

def validate_worksheet(doc_path: str) -> bool:
    """Validiert ein erstelltes Arbeitsblatt."""
    doc = Document(doc_path)
    errors = []
    
    # Gesamttext sammeln
    all_text = ""
    for p in doc.paragraphs:
        all_text += p.text + "\n"
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                all_text += cell.text + "\n"
    
    # Check 1: Nicht ersetzte Platzhalter
    placeholders = re.findall(r'\[[^\]]+\]', all_text)
    real_placeholders = [p for p in placeholders if p not in ['[]']]
    if real_placeholders:
        errors.append(f"❌ PLATZHALTER NICHT ERSETZT: {real_placeholders}")
    
    # Check 2: Falsche Umlaute
    umlaut_words = [
        'fuehren', 'koennen', 'muessen', 'waehlen', 'naechste',
        'aehnlich', 'ueber', 'fuer', 'Schueler', 'Pruefung', 
        'Uebung', 'erklaeren', 'begruenden'
    ]
    found_errors = [w for w in umlaut_words if w.lower() in all_text.lower()]
    if found_errors:
        errors.append(f"❌ UMLAUT-FEHLER: {found_errors}")
    
    # Ergebnis
    if errors:
        print("\n".join(errors))
        return False
    print(f"✅ Validiert: {doc_path}")
    return True
```

---

## Differenzierung (Niveaus)

| Niveau | Code | Beschreibung | Anpassungen |
|--------|------|--------------|-------------|
| Anfänger | A | Mehr Hilfestellung | Wortbanken, Satzanfänge, Beispiele |
| Fortgeschritten | B | Standard | Normale Aufgabenstellung |
| Experte | C | Erweitert | Weniger Scaffolding, komplexer |

### Bei differenzierten ABs: Separate Dateien!

```
AB_01_PassiveVoice_NiveauA.docx  ← Mit Hilfsboxen
AB_01_PassiveVoice_NiveauB.docx  ← Standard
AB_01_PassiveVoice_NiveauC.docx  ← Erweitert
```

---

## Dateinamen-Konventionen

| Typ | Format | Beispiel |
|-----|--------|----------|
| Arbeitsblatt | `AB_[Nr]_[Thema].docx` | `AB_01_PassiveVoice.docx` |
| Differenziert | `AB_[Nr]_[Thema]_Niveau[A/B/C].docx` | `AB_01_PassiveVoice_NiveauA.docx` |
| Klassenarbeit | `KA_[Nr]_[Thema].docx` | `KA_02_Unit3Travel.docx` |

---

## Integration mit anderen Skills

| Skill | Verwendung |
|-------|------------|
| `docx` (public) | **PFLICHT** - Technische Grundlage |
| `unterrichtsstunde-erstellen-v2` | PowerPoint zur gleichen Stunde |
| `vokabeln-zusammenfassen` | Vocabulary Sheet (nur Englisch) |
| `unterrichtsplanung-workflow` | Liefert die Stundenplanung |

---

## Checkliste vor Abgabe

- [ ] Passende Vorlage verwendet (AB vs. KA)
- [ ] **ALLE** Header-Platzhalter ersetzt
- [ ] **Umlaute korrekt** (ä/ö/ü/ß, NICHT ae/oe/ue/ss)
- [ ] Lernziele max. ~60 Zeichen
- [ ] Niveau = NUR ein Buchstabe (A, B oder C)
- [ ] Body-Inhalt vollständig
- [ ] Dateiname folgt Konvention
- [ ] `validate_worksheet()` bestanden

---

## Changelog

| Version | Datum | Änderungen |
|---------|-------|------------|
| 2.0.0 | 24.01.2025 | Komplette Neugestaltung: Bereinigte Vorlagen, Body-Ersetzung, zwei Vorlagen |
