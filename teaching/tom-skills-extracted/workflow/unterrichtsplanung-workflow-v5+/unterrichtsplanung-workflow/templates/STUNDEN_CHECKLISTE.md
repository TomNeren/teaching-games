# STUNDEN_CHECKLISTE Template

**Version:** 5.0 (29.01.2026)
**Zweck:** Validierungs-Checkliste nach jeder erstellten Stunde

---

## Verwendung

Diese Checkliste wird von Cowork nach JEDER erstellten Stunde ausgefüllt. Sie dient der Qualitätssicherung und dokumentiert den Erstellungsstatus.

---

# Checkliste (Copy-Paste-fähig)

```markdown
## ✅ Checkliste Stunde {{NR}}: {{THEMA}}

**Projekt:** {{PROJEKT_ID}}
**Erstellt:** {{DATUM_UHRZEIT}}

---

### 📄 Arbeitsblätter

| Datei | Erstellt | Validiert | Fehler |
|-------|----------|-----------|--------|
| `AB_{{NR}}_{{TITEL}}.docx` | ☐ | ☐ | |
| `AB_{{NR}}_{{TITEL}}_NiveauA.docx` | ☐ | ☐ | |

**Validierungsprüfungen:**
- [ ] Vorlage korrekt geladen: `Vorlage_Fach.docx` (aus arbeitsblatt-erstellen-v3!)
- [ ] ALLE Platzhalter ersetzt (keine `[...]` mehr)
- [ ] Umlaute korrekt (ä/ö/ü/ß, NICHT ae/oe/ue/ss)
- [ ] Lernziele max. 60 Zeichen pro Zeile
- [ ] Niveau korrekt gesetzt (A, B oder C - NUR EIN Buchstabe!)
- [ ] Dateiname folgt Konvention
- [ ] `validate_worksheet()` ausgeführt: ✅ / ❌

**Validierungsausgabe:**
```
{{VALIDATION_OUTPUT_AB}}
```

---

### 🖼️ Bilder

| ID | Prompt | Tool | Generiert | Eingefügt | Fehler |
|----|--------|------|-----------|-----------|--------|
| `IMG_{{NR}}_01` | {{PROMPT_1}} | ComfyUI/Fallback | ☐ | ☐ | |
| `IMG_{{NR}}_02` | {{PROMPT_2}} | ComfyUI/Fallback | ☐ | ☐ | |

**Bild-Prüfungen:**
- [ ] ComfyUI Status geprüft (mcp__Control_your_Mac__osascript)
- [ ] Primär: `mcp__comfyui__generate_image` aufgerufen
- [ ] Bei Fehler: Fallback verwendet (nanobanana / HF)
- [ ] Format korrekt: 1024x576 (16:9) oder 1024x1024 (1:1)
- [ ] Bilder heruntergeladen
- [ ] Bilder in Zielordner kopiert
- [ ] Bilder in Dokumente eingefügt
- [ ] Bilder in PPT eingefügt

---

### 📊 PowerPoint

| Datei | Erstellt | Validiert | Fehler |
|-------|----------|-----------|--------|
| `Stunde_{{NR}}_PPT.pptx` | ☐ | ☐ | |

**Validierungsprüfungen:**
- [ ] Vorlage korrekt geladen: `Vorlage.pptx` (aus unterrichtsstunde-erstellen-v3!)
- [ ] Folienanzahl korrekt: {{ANZAHL_IST}} / {{ANZAHL_SOLL}}
- [ ] Timer-Videos (mp4!) eingefügt: {{TIMER_ANZAHL}}
- [ ] Timer aus korrektem Ordner: `timer_pixel_schnee/`
- [ ] Arbeitsaufträge OBEN auf Timer-Folien
- [ ] Fonts korrigiert (keine +mj-lt, +mn-lt)
- [ ] Mindestschriftgröße 20pt eingehalten
- [ ] Umlaute korrekt (ä/ö/ü/ß)
- [ ] Bilder eingefügt (wenn definiert)
- [ ] Dateiname folgt Konvention
- [ ] `validate_presentation()` ausgeführt: ✅ / ❌

**Validierungsausgabe:**
```
{{VALIDATION_OUTPUT_PPT}}
```

---

### 📁 Dateien

**Speicherort:** `{{OUTPUT_PFAD}}`

| Datei | Existiert | Größe |
|-------|-----------|-------|
| `AB_{{NR}}_{{TITEL}}.docx` | ☐ | {{SIZE}} |
| `Stunde_{{NR}}_PPT.pptx` | ☐ | {{SIZE}} |
| `IMG_{{NR}}_01.webp` | ☐ | {{SIZE}} |

**Ordnerstruktur korrekt:**
- [ ] `/Stunde_{{NR}}/` erstellt
- [ ] `/Stunde_{{NR}}/doc/` erstellt
- [ ] Dateien an richtiger Stelle

---

### 📋 Status

| Aspekt | Status |
|--------|--------|
| Arbeitsblätter | 🟢 Fertig / 🟡 Teilweise / 🔴 Fehler |
| Bilder | 🟢 Fertig / 🟡 Teilweise / 🔴 Fehler / ⚪ N/A |
| PowerPoint | 🟢 Fertig / 🟡 Teilweise / 🔴 Fehler |
| Dateisystem | 🟢 Fertig / 🟡 Teilweise / 🔴 Fehler |

**Gesamtstatus Stunde {{NR}}:** 🟢 / 🟡 / 🔴

---

### 📝 Notizen

**Probleme:**
{{PROBLEME}}

**Abweichungen vom Protokoll:**
{{ABWEICHUNGEN}}

**Verbesserungsvorschläge:**
{{VERBESSERUNGEN}}

---

*Checkliste ausgefüllt: {{TIMESTAMP}}*
```

---

## Kompakte Version (für schnelle Validierung)

```markdown
## ✅ Stunde {{NR}} - Quick Check

| Material | ✓ | Validiert | Fehler |
|----------|---|-----------|--------|
| AB Standard | ☐ | ☐ | |
| AB Niveau A | ☐ | ☐ | |
| Bilder | ☐ | ☐ | |
| PPT | ☐ | ☐ | |

**Kritische Prüfungen:**
- [ ] Keine `[...]` Platzhalter übrig
- [ ] Keine ae/oe/ue Fehler
- [ ] Timer-Arbeitsaufträge OBEN
- [ ] Timer sind mp4-Format
- [ ] Folienanzahl = {{SOLL}}
- [ ] ComfyUI geschlossen

**Status:** 🟢 / 🟡 / 🔴
```

---

## Automatische Validierungsfunktionen

### Für Arbeitsblätter (v3)

```python
def validate_worksheet(doc_path: str) -> bool:
    """
    Validiert ein erstelltes Arbeitsblatt.
    Prüft: Platzhalter, Umlaute, Encoding
    """
    from docx import Document
    import re

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

    # Check 1: Platzhalter
    placeholders = re.findall(r'\[[^\]]+\]', all_text)
    real_placeholders = [p for p in placeholders if p not in ['[]']]
    if real_placeholders:
        errors.append(f"❌ PLATZHALTER NICHT ERSETZT: {real_placeholders}")

    # Check 2: Falsche Umlaute
    umlaut_words = [
        'fuehren', 'koennen', 'muessen', 'waehlen', 'naechste',
        'aehnlich', 'ueber', 'fuer', 'Ausfuehren', 'Taetigkeit',
        'koennte', 'muesste', 'wuerde', 'haette', 'waere',
        'Schueler', 'Pruefung', 'Uebung', 'erklaeren', 'begruenden'
    ]
    found_errors = [w for w in umlaut_words if w.lower() in all_text.lower()]
    if found_errors:
        errors.append(f"❌ UMLAUT-FEHLER: {found_errors}")

    # Ergebnis
    if errors:
        print("\n".join(errors))
        return False
    else:
        print(f"✅ AB validiert: {doc_path}")
        return True
```

### Für PowerPoints (v3)

```python
def validate_presentation(pptx_path: str, expected_slides: int, expected_timers: int) -> bool:
    """
    Validiert eine erstellte Präsentation.
    Prüft: Folienanzahl, Timer (mp4!), Umlaute, Fonts
    """
    from pptx import Presentation

    prs = Presentation(pptx_path)
    errors = []

    # Check 1: Folienanzahl
    actual_slides = len(prs.slides)
    if actual_slides != expected_slides:
        errors.append(f"❌ FOLIENANZAHL: {actual_slides} (erwartet: {expected_slides})")

    # Check 2: Videos/Timer zählen (mp4!)
    video_count = 0
    for slide in prs.slides:
        for shape in slide.shapes:
            if hasattr(shape, "media_type"):
                video_count += 1

    if video_count < expected_timers:
        errors.append(f"❌ TIMER/VIDEOS (mp4): {video_count} (erwartet: min. {expected_timers})")

    # Check 3: Font-Check
    bad_fonts = set()
    for slide in prs.slides:
        for shape in slide.shapes:
            if shape.has_text_frame:
                for para in shape.text_frame.paragraphs:
                    for run in para.runs:
                        if run.font.name and run.font.name.startswith('+'):
                            bad_fonts.add(run.font.name)

    if bad_fonts:
        errors.append(f"❌ NICHT KORRIGIERTE FONTS: {bad_fonts}")

    # Check 4: Umlaut-Check
    all_text = ""
    for slide in prs.slides:
        for shape in slide.shapes:
            if shape.has_text_frame:
                for para in shape.text_frame.paragraphs:
                    all_text += para.text + "\n"

    umlaut_words = ['fuehren', 'koennen', 'Ausfuehren', 'naechste', 'fuer',
                    'muessen', 'waehlen', 'Taetigkeit', 'wuerde', 'haette']
    found_errors = [w for w in umlaut_words if w.lower() in all_text.lower()]
    if found_errors:
        errors.append(f"❌ UMLAUT-FEHLER: {found_errors}")

    # Ergebnis
    if errors:
        print("\n".join(errors))
        return False
    else:
        print(f"✅ PPT validiert: {pptx_path}")
        print(f"   Folien: {actual_slides}, Videos/Timer: {video_count}")
        return True
```

---

## Zusammenfassungs-Checkliste (nach allen Stunden)

```markdown
## 📋 Projekt-Zusammenfassung: {{PROJEKT_ID}}

### Stunden-Status

| Stunde | Thema | AB | Bilder | PPT | Status |
|--------|-------|----|----|-----|--------|
| 1 | {{THEMA_1}} | ✅ | ✅ | ✅ | 🟢 |
| 2 | {{THEMA_2}} | ✅ | ⚪ | ✅ | 🟢 |
| 3 | {{THEMA_3}} | ✅ | ✅ | 🟡 | 🟡 |

### Zusatzmaterialien

| Material | Erstellt | Validiert |
|----------|----------|-----------|
| Self-Assessment | ☐ | ☐ |
| Vokabelliste (EN) | ☐ | ☐ |

### ComfyUI Status

- [ ] ComfyUI gestartet (mcp__Control_your_Mac__osascript)
- [ ] Alle Bilder generiert (mcp__comfyui__generate_image)
- [ ] ComfyUI geschlossen

### Gesamtergebnis

- **Erstellt:** {{ANZAHL_ERSTELLT}} / {{ANZAHL_GEPLANT}} Materialien
- **Validiert:** {{ANZAHL_VALIDIERT}} / {{ANZAHL_ERSTELLT}}
- **Fehler:** {{ANZAHL_FEHLER}}

### Dateien übergeben

```
{{OUTPUT_PFAD}}/
├── Stunde_01/ ✅
├── Stunde_02/ ✅
├── Stunde_03/ 🟡
└── Self_Assessment_{{EINHEIT}}.docx ✅
```

**Projektstatus:** 🟢 Abgeschlossen / 🟡 Teilweise / 🔴 Fehler

---

*Zusammenfassung erstellt: {{TIMESTAMP}}*
```

---

## Version History

| Version | Datum | Änderungen |
|---------|-------|------------|
| 1.0 | 22.01.2025 | Initiale Erstellung mit Validierungsfunktionen |
| 4.0 | 24.01.2025 | v2-Validierungsfunktionen, Font-Check |
| **5.0** | **29.01.2026** | **v3-Skills, MCP-Tool-Namen (mcp__...), Timer mp4, ComfyUI-Status mit osascript** |
