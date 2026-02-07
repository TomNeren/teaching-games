---
name: arbeitsblatt-erstellen-v3
description: Erstellt ALLE Word-Dokumente (.docx) für den Unterricht - Arbeitsblätter, Infoblätter, Handouts, Materialien, Country Profiles, Crisis Briefings. IMMER diese Vorlage verwenden wenn .docx für Schüler erstellt wird.
---

# Skill: Arbeitsblatt erstellen (v3)

**Version:** 3.0.0
**Stand:** 27.01.2026
**Changelog:** Erweiterte Trigger, PFLICHT-Nutzung für alle Unterrichts-.docx, klare Entscheidungslogik

---

## ⚠️ PFLICHT-CHECK VOR JEDER .DOCX-ERSTELLUNG

```
┌─────────────────────────────────────────────────────────────────┐
│  🚨 STOP! BEVOR DU .DOCX ERSTELLST:                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. Ist dies ein Dokument für Schüler/Unterricht?              │
│     ├── JA  → DIESEN SKILL NUTZEN (Vorlage laden!)             │
│     └── NEIN → Generisches docx-Skill nutzen                   │
│                                                                 │
│  2. Welche Vorlage passt?                                       │
│     ├── Arbeitsblatt/Infoblatt/Handout → Vorlage_Fach.docx     │
│     └── Klassenarbeit/Test            → Vorlage_Klassenarbeit  │
│                                                                 │
│  3. Hast du die Vorlage GELADEN?                                │
│     ├── JA  → Weiter mit Platzhalter-Ersetzung                 │
│     └── NEIN → STOPP! Erst Vorlage laden!                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**NIEMALS** eigene .docx-Dateien von Grund auf erstellen wenn dieser Skill verfügbar ist!

---

## Zweck

Erstellt **ALLE** Word-Dokumente für den Unterricht mit einheitlichem Design-System:
- Arbeitsblätter
- Infoblätter / Expert Group Materials
- Handouts
- Country Profiles
- Crisis Briefings
- Structured Notes
- Position Matrices
- Phrase Sheets
- Klassenarbeiten / Tests

---

## 🎯 TRIGGER (ERWEITERT in v3)

### Explizite Trigger
- "erstelle Arbeitsblatt", "AB erstellen"
- "erstelle Klassenarbeit", "Test erstellen"
- "erstelle Infoblatt", "Infoblätter erstellen"
- "erstelle Handout", "Materialien erstellen"
- "erstelle Word-Dokument für Unterricht"
- "Worksheet erstellen"

### Implizite Trigger (AUTOMATISCH aktivieren!)
- Übergabeprotokoll enthält `.docx` Dateien
- Materialübersicht listet Word-Dokumente
- Begriffe: "Country Profile", "Crisis Briefing", "Structured Notes", "Position Matrix", "Phrase Sheet"
- Jede Anfrage für Schüler-Materialien im .docx Format

### NICHT verwenden bei:
- Persönliche Notizen des Lehrers
- Administrative Dokumente
- Reine Text-Exports ohne Formatierung

---

## Dateien in diesem Skill

```
/mnt/skills/user/arbeitsblatt-erstellen-v3/
├── SKILL.md                           ← Diese Datei
├── templates/
│   ├── Vorlage_Fach.docx             ← Alle Unterrichtsmaterialien
│   └── Vorlage_Klassenarbeit.docx    ← Tests/Klassenarbeiten
└── scripts/
    └── create_worksheet.py           ← Automatisierte Erstellung
```

---

## Design-System

### Header-Struktur (Vorlage_Fach.docx)

```
┌─────────────────────────────────────┬─────────────┬──────────────┐
│ Arbeitsblatt / Infoblatt            │   [LOGO]    │              │
│ [Thema]                             │             │              │
├─────────────────────────────────────┼─────────────┼──────────────┤
│ Lernziele:                          │   [Fach]    │ Niveau:      │
│ [Ziel 1]                            │             │ [A / B / C]  │
│ [Ziel 2]                            │             │              │
│ [Ziel 3]                            │             │              │
├─────────────────────────────────────┼─────────────┴──────────────┤
│ Name:            Vorname:           │ Datum:                     │
└─────────────────────────────────────┴────────────────────────────┘
```

### Typografie

| Element | Schriftart | Größe | Hinweis |
|---------|------------|-------|---------|
| Header | Avenir Next | Aus Vorlage | Logo, Fach, Niveau |
| Normal | Avenir Next | 11pt | Body-Text, Listen |
| Heading 1 | Avenir Next Ultra Light | 16pt | Hauptüberschriften, unterstrichen |
| Heading 2 | Avenir Next Medium | 13pt | Unterüberschriften, unterstrichen |

---

## Vorlagen-Platzhalter

### Vorlage_Fach.docx

| Platzhalter | Beschreibung | Beispiel | Max. Länge |
|-------------|--------------|----------|------------|
| `[Thema]` | Titel des Dokuments | "NATO Foundations" | ~50 Zeichen |
| `[Fach]` | Unterrichtsfach | "Englisch", "GGK" | ~15 Zeichen |
| `[Ziel 1 – nicht länger als eine Zeile]` | Lernziel 1 | "I can explain Article 5" | ~60 Zeichen |
| `[Ziel 2 – nicht länger als eine Zeile]` | Lernziel 2 | "I can summarize key facts" | ~60 Zeichen |
| `[Ziel 3 – nicht länger als eine Zeile]` | Lernziel 3 | "I can teach peers" | ~60 Zeichen |
| `[A / B / C]` | Niveau (NUR ein Buchstabe!) | "B" | 1 Zeichen |

### Vorlage_Klassenarbeit.docx

| Platzhalter | Beschreibung | Beispiel |
|-------------|--------------|----------|
| `Klassenarbeit [1/2/3/4]` | Nummer ersetzen | "Klassenarbeit 2" |
| `[Thema]` | Titel der Arbeit | "Unit 3: NATO Security" |
| `[Fach]` | Unterrichtsfach | "Englisch" |
| `[abhängig von Aufbau]` | Maximale Punktzahl | "45" |
| `[A / B / C]` | Niveau | "B" |

---

## ⚡ KRITISCHE REGELN

### 1. ENCODING (Umlaute) - IMMER!

```
✅ RICHTIG: ä, ö, ü, ß, Ä, Ö, Ü
❌ FALSCH:  ae, oe, ue, ss, Ae, Oe, Ue

NIEMALS ae/oe/ue verwenden! Immer echte Umlaute!
```

### 2. Platzhalter VOLLSTÄNDIG ersetzen

```
Nach Erstellung darf KEIN [...] mehr im Header sein!
→ Validierung nach JEDEM Dokument ausführen
```

### 3. Niveau: NUR EIN Buchstabe

```
✅ RICHTIG: "B"
❌ FALSCH:  "A / B / C" oder "Niveau B"
```

### 4. VORLAGE IMMER LADEN

```
❌ FALSCH: Document() → neues leeres Dokument
✅ RICHTIG: Document(TEMPLATE_PATH) → Vorlage laden
```

---

## Erstellungs-Strategie

### Konzept: Header ersetzen, Body komplett neu

```
VORHER (Vorlage):
├── Header (Tabelle) → Platzhalter ersetzen
└── Body             → Beispieltext "Erarbeitungsphase 1..."

NACHHER (Fertiges Dokument):
├── Header (Tabelle) → Mit echten Werten gefüllt
└── Body             → Komplett neuer Inhalt aus Protokoll/Planung
```

---

## Python-Workflow

### 1. Basis-Pfade (IMMER diese verwenden!)

```python
from pathlib import Path
from docx import Document

# SKILL PFADE - NICHT ÄNDERN!
SKILL_PATH = Path("/mnt/skills/user/arbeitsblatt-erstellen-v3")
TEMPLATE_AB = SKILL_PATH / "templates" / "Vorlage_Fach.docx"
TEMPLATE_KA = SKILL_PATH / "templates" / "Vorlage_Klassenarbeit.docx"
```

### 2. Vorlage laden (PFLICHT!)

```python
# ✅ RICHTIG: Vorlage laden
doc = Document(str(TEMPLATE_AB))

# ❌ FALSCH: Leeres Dokument erstellen
doc = Document()  # NIEMALS bei Unterrichtsmaterialien!
```

### 3. Header-Platzhalter ersetzen

```python
def replace_header_placeholders(doc, replacements: dict):
    """Ersetzt Platzhalter in Header-Tabellen."""
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
    return doc

# Verwendung
replacements = {
    '[Thema]': 'NATO Foundations – Collective Defence',
    '[Fach]': 'Englisch',
    '[Ziel 1 – nicht länger als eine Zeile]': 'I can explain Article 5',
    '[Ziel 2 – nicht länger als eine Zeile]': 'I can summarize NATO history',
    '[Ziel 3 – nicht länger als eine Zeile]': 'I can teach key facts to peers',
    '[A / B / C]': 'B',
}
doc = replace_header_placeholders(doc, replacements)
```

### 4. Body löschen und neu schreiben

```python
def clear_body(doc):
    """Entfernt alle Paragraphen nach dem ersten."""
    while len(doc.paragraphs) > 1:
        p = doc.paragraphs[-1]._element
        p.getparent().remove(p)
    if doc.paragraphs:
        doc.paragraphs[0].clear()
    return doc

# Body löschen
doc = clear_body(doc)

# Neuen Inhalt einfügen (nutzt Document Styles!)
p = doc.add_paragraph("Part 1: The Washington Treaty", style='Heading 1')
p.runs[0].underline = True

p = doc.add_paragraph("Read the text and summarize the key points.", style='Normal')
```

### 5. Validierung (PFLICHT!)

```python
import re

def validate_document(doc_path: str) -> bool:
    """Validiert ein erstelltes Dokument."""
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
    if placeholders:
        errors.append(f"❌ PLATZHALTER NICHT ERSETZT: {placeholders}")

    # Check 2: Falsche Umlaute
    umlaut_errors = ['ae', 'oe', 'ue', 'Ae', 'Oe', 'Ue']
    for ue in umlaut_errors:
        if ue in all_text:
            errors.append(f"❌ UMLAUT-FEHLER: '{ue}' gefunden")

    # Ergebnis
    if errors:
        print("\n".join(errors))
        return False
    print(f"✅ Validiert: {doc_path}")
    return True

# IMMER nach Erstellung aufrufen!
validate_document(output_path)
```

---

## Komplettes Beispiel: Infoblatt erstellen

```python
from pathlib import Path
from docx import Document
from docx.shared import Inches

# === 1. KONFIGURATION ===
SKILL_PATH = Path("/mnt/skills/user/arbeitsblatt-erstellen-v3")
TEMPLATE_AB = SKILL_PATH / "templates" / "Vorlage_Fach.docx"
OUTPUT_PATH = "/mnt/user-data/outputs/INFO_01_NATO_Foundations.docx"

# === 2. VORLAGE LADEN ===
doc = Document(str(TEMPLATE_AB))

# === 3. HEADER ERSETZEN ===
replacements = {
    '[Thema]': 'NATO Foundations – Collective Defence & Decision-Making',
    '[Fach]': 'Englisch',
    '[Ziel 1 – nicht länger als eine Zeile]': 'I can explain Article 5 and its implications',
    '[Ziel 2 – nicht länger als eine Zeile]': 'I can describe NATO decision-making',
    '[Ziel 3 – nicht länger als eine Zeile]': 'I can teach key facts to my peers',
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

# === 4. BODY LÖSCHEN ===
while len(doc.paragraphs) > 1:
    p = doc.paragraphs[-1]._element
    p.getparent().remove(p)
if doc.paragraphs:
    doc.paragraphs[0].clear()

# === 5. NEUEN INHALT EINFÜGEN ===
# Überschrift
p = doc.add_paragraph("The Washington Treaty (1949)", style='Heading 1')
p.runs[0].underline = True

# Fließtext
doc.add_paragraph("""In the aftermath of World War II, Western nations watched with growing alarm as Soviet influence spread across Eastern Europe. The Berlin Blockade of 1948-49 crystallised fears of communist expansion, prompting twelve nations to sign the North Atlantic Treaty in Washington on April 4, 1949.""")

# Weitere Überschrift
p = doc.add_paragraph("Article 5: The Heart of NATO", style='Heading 1')
p.runs[0].underline = True

doc.add_paragraph("""Article 5 contains NATO's famous collective defence guarantee: "An armed attack against one or more of them in Europe or North America shall be considered an attack against them all." However, the precise commitment is often misunderstood...""")

# === 6. SPEICHERN ===
doc.save(OUTPUT_PATH)
print(f"✅ Gespeichert: {OUTPUT_PATH}")

# === 7. VALIDIEREN ===
# validate_document(OUTPUT_PATH)  # Immer aufrufen!
```

---

## Dateinamen-Konventionen

| Typ | Format | Beispiel |
|-----|--------|----------|
| Infoblatt | `INFO_[Nr]_[Thema].docx` | `INFO_01_NATO_Foundations.docx` |
| Arbeitsblatt | `AB_[Nr]_[Thema].docx` | `AB_01_PassiveVoice.docx` |
| Country Profile | `COUNTRY_[Nr]_[Land].docx` | `COUNTRY_05_Poland.docx` |
| Crisis Briefing | `CRISIS_[Nr]_[Titel].docx` | `CRISIS_01_Baltic_Shield.docx` |
| Structured Notes | `NOTES_[Beschreibung].docx` | `NOTES_Structured_Notes.docx` |
| Phrases | `PHRASES_[Beschreibung].docx` | `PHRASES_Diplomatic_Language.docx` |
| Matrix | `MATRIX_[Beschreibung].docx` | `MATRIX_Position_Matrix.docx` |
| Klassenarbeit | `KA_[Nr]_[Thema].docx` | `KA_02_Unit3Travel.docx` |
| Differenziert | `[Typ]_[Nr]_[Thema]_Niveau[A/B/C].docx` | `AB_01_PassiveVoice_NiveauA.docx` |

---

## Checkliste vor Abgabe

- [ ] **VORLAGE GELADEN** (nicht leeres Dokument erstellt)
- [ ] Passende Vorlage verwendet (Fach vs. Klassenarbeit)
- [ ] **ALLE** Header-Platzhalter ersetzt
- [ ] **Umlaute korrekt** (ä/ö/ü/ß, NICHT ae/oe/ue/ss)
- [ ] Lernziele max. ~60 Zeichen
- [ ] Niveau = NUR ein Buchstabe (A, B oder C)
- [ ] Body-Inhalt vollständig
- [ ] Dateiname folgt Konvention
- [ ] **validate_document() bestanden**

---

## Integration mit anderen Skills

| Skill | Beziehung |
|-------|-----------|
| **docx (public)** | Technische Grundlage - PFLICHT lesen |
| **unterrichtsstunde-erstellen-v3** | PowerPoint zur gleichen Stunde |
| **vokabeln-zusammenfassen** | Vocabulary Sheet (nur Englisch) |
| **unterrichtsplanung-workflow** | Liefert die Stundenplanung/Handover |
| **unterrichts-medien** | Bilder für Arbeitsblätter |

---

## Version History

| Version | Datum | Änderungen |
|---------|-------|------------|
| 2.0.0 | 24.01.2025 | Bereinigte Vorlagen, Body-Ersetzung |
| **3.0.0** | **27.01.2026** | **Erweiterte Trigger (Infoblätter, Country Profiles, etc.), PFLICHT-Check, klare Entscheidungslogik, verbesserte Dokumentation** |
