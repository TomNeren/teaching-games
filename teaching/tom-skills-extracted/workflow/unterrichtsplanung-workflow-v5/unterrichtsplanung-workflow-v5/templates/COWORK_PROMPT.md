# COWORK_PROMPT Template

**Version:** 4.0 (24.01.2025)
**Zweck:** Direkter Ausführungsbefehl für Cowork (Copy-Paste-fähig)

---

## Verwendung

Dieser Prompt wird am Ende der Chat-Planung erstellt und direkt in Cowork eingefügt. Er aktiviert die nötigen Skills und definiert die Ausführungsreihenfolge.

---

# Cowork-Prompt (Copy-Paste-Vorlage)

```markdown
# 🚀 Materialerstellung: {{PROJEKT_ID}}

## Anweisung

Du erhältst ein Übergabeprotokoll mit vollständig ausformulierten Inhalten. Deine Aufgabe ist die TECHNISCHE UMSETZUNG - die Texte sind bereits fertig!

---

## 1️⃣ SKILLS LESEN (PFLICHT!)

Lies ZUERST diese Skills:

```bash
view /mnt/skills/user/arbeitsblatt-erstellen-v2/SKILL.md
view /mnt/skills/user/unterrichtsstunde-erstellen-v2/SKILL.md
view /mnt/skills/public/docx/SKILL.md
```

---

## 2️⃣ COMFYUI STARTEN

```bash
open -a "ComfyUI"

# Warten bis Server bereit
until curl -s http://127.0.0.1:8188 > /dev/null; do
    echo "Warte auf ComfyUI..."
    sleep 2
done
echo "ComfyUI bereit!"
```

---

## 3️⃣ PRO STUNDE ABARBEITEN

### Reihenfolge für JEDE Stunde:

#### A) Arbeitsblätter erstellen
1. Vorlage laden: `/mnt/skills/user/arbeitsblatt-erstellen-v2/templates/Vorlage_Fach.docx`
2. ALLE Platzhalter ersetzen (aus Protokoll-Tabelle)
3. Body-Inhalt aus Protokoll einfügen (FERTIGE Texte!)
4. **VALIDIEREN** (Platzhalter, Umlaute)
5. Speichern mit Konvention: `AB_{{NR}}_{{Titel}}.docx`

#### B) Bilder generieren
1. ComfyUI verwenden: `comfyui:generate_image`
   - prompt: aus Protokoll
   - width: 1280, height: 720
2. Bei Fehler → Fallback: `nanobanana:generate_image`
3. Bei Fehler → Fallback: `Hugging Face:gr4_z_image_turbo_generate`
4. Bilder in Zielordner speichern

#### C) PowerPoint erstellen
1. Vorlage laden: `/mnt/skills/user/unterrichtsstunde-erstellen-v2/Vorlage.pptx`
2. Folien gemäß Protokoll-Struktur erstellen
3. Timer-Videos einfügen (intern: 4, 5, 10 min; extern: andere)
4. Generierte Bilder einfügen
5. Fonts korrigieren (fix_fonts)
6. **VALIDIEREN**
7. Speichern: `Stunde_{{NR}}_PPT.pptx`

#### D) Stunden-Checkliste ausfüllen
→ Template: `/mnt/skills/user/unterrichtsplanung-workflow/templates/STUNDEN_CHECKLISTE.md`

---

## 4️⃣ COMFYUI SCHLIEßEN

```bash
osascript -e 'quit app "ComfyUI"'
```

---

## 5️⃣ NACH ALLEN STUNDEN

### Für Englisch:
- [ ] Vokabelliste erstellen (aus fertigen Materialien extrahieren)

### Für alle Fächer:
- [ ] Self-Assessment erstellen
- [ ] Abschluss-Report

---

## ⚠️ KRITISCHE REGELN

### Encoding (NIEMALS vergessen!)
```
✅ RICHTIG: ä, ö, ü, ß, Ä, Ö, Ü
❌ FALSCH:  ae, oe, ue, ss
```

### Platzhalter
```
Nach Erstellung darf KEIN [...] mehr im Dokument sein!
```

### Timer-Folien
```
Arbeitsauftrag OBEN, Timer unten!
```

### Niveau
```
NUR ein Buchstabe: A, B oder C
```

---

## 📁 Output-Ordner

```
{{ICLOUD_PFAD}}/{{KLASSE}}/{{EINHEIT}}/
├── Stunde_01/
│   ├── doc/
│   │   └── AB_01_{{Titel}}.docx
│   └── Stunde_01_PPT.pptx
├── Stunde_02/
│   └── ...
└── Self_Assessment_{{EINHEIT}}.docx
```

---

## Validierungsfunktionen

### Für Arbeitsblätter:
```python
def validate_worksheet(doc_path):
    # Prüft: Platzhalter, Umlaute
    # Siehe arbeitsblatt-erstellen-v2 SKILL.md
```

### Für PowerPoints:
```python
def validate_presentation(pptx_path, expected_slides, expected_timers):
    # Prüft: Folienanzahl, Timer, Umlaute
    # Siehe unterrichtsstunde-erstellen-v2 SKILL.md
```

---

*Los geht's! Beginne mit Schritt 1: Skills lesen.*
```

---

## Version History

| Version | Datum | Änderungen |
|---------|-------|------------|
| 1.0 | 18.01.2025 | Initiale Erstellung |
| 2.0 | 22.01.2025 | Stunden-Checkliste integriert |
| **4.0** | **24.01.2025** | **v2-Skills, ComfyUI-Automation, Fallback-Kaskade** |
