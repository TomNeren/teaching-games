# COWORK_PROMPT Template

**Version:** 5.0 (29.01.2026)
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

## 🚨 SKILL-PFLICHT-CHECK (IMMER ZUERST!)

| Dateityp | Skill | Vorlage/Tool |
|----------|-------|--------------|
| .docx | arbeitsblatt-erstellen-v3 | Vorlage_Fach.docx |
| .pptx | unterrichtsstunde-erstellen-v3 | Vorlage.pptx |
| Bilder | unterrichts-medien | mcp__comfyui__generate_image |
| Timer | - | timer_pixel_schnee/ (mp4!) |

⚠️ NIEMALS eigene Scripts von Grund auf erstellen!
⚠️ IMMER zuerst die Skills lesen und Vorlagen laden!

---

## 1️⃣ SKILLS LESEN (PFLICHT!)

Lies ZUERST diese Skills:

```bash
view /mnt/skills/user/arbeitsblatt-erstellen-v3/SKILL.md
view /mnt/skills/user/unterrichtsstunde-erstellen-v3/SKILL.md
view /mnt/skills/user/unterrichts-medien/SKILL.md
```

---

## 2️⃣ COMFYUI STARTEN

```javascript
// 1. Status prüfen
mcp__Control_your_Mac__osascript({
  script: 'do shell script "curl -s -m 5 http://127.0.0.1:8188/system_stats"'
})

// 2. Falls nicht läuft: Starten
mcp__Control_your_Mac__osascript({
  script: 'do shell script "cd ~/ComfyUI && source venv/bin/activate && python main.py --use-pytorch-cross-attention --force-fp16 &> /tmp/comfyui.log &\necho started"'
})

// 3. Warten (8 Sek)
mcp__Control_your_Mac__osascript({
  script: 'delay 8'
})
```

---

## 3️⃣ PRO STUNDE ABARBEITEN

### Reihenfolge für JEDE Stunde:

#### A) Arbeitsblätter erstellen
1. Vorlage laden: `/mnt/skills/user/arbeitsblatt-erstellen-v3/templates/Vorlage_Fach.docx`
2. ALLE Platzhalter ersetzen (aus Protokoll-Tabelle)
3. Body-Inhalt aus Protokoll einfügen (FERTIGE Texte!)
4. **VALIDIEREN** (Platzhalter, Umlaute)
5. Speichern mit Konvention: `AB_{{NR}}_{{Titel}}.docx`

#### B) Bilder generieren
1. ComfyUI verwenden: `mcp__comfyui__generate_image`
   - prompt: aus Protokoll
   - width: 1024, height: 576 (16:9)
2. Bei Fehler → Fallback: `mcp__nanobanana__generate_image`
3. Bei Fehler → Fallback: `mcp__fa86031e-8beb-4aac-b517-e3b796ddf8ec__gr4_z_image_turbo_generate`
4. Bilder in Zielordner speichern

#### C) PowerPoint erstellen
1. Vorlage laden: `/mnt/skills/user/unterrichtsstunde-erstellen-v3/Vorlage.pptx`
2. Folien gemäß Protokoll-Struktur erstellen
3. Timer-Videos (mp4!) einfügen aus:
   `/Users/tomren/Library/CloudStorage/GoogleDrive-renne.tom@googlemail.com/Meine Ablage/Claude-Meta-Projekt/ppt_update/timer_pixel_schnee/`
4. Generierte Bilder einfügen
5. Fonts korrigieren (fix_fonts)
6. **VALIDIEREN**
7. Speichern: `Stunde_{{NR}}_PPT.pptx`

#### D) Stunden-Checkliste ausfüllen
→ Template: `/mnt/skills/user/unterrichtsplanung-workflow/templates/STUNDEN_CHECKLISTE.md`

---

## 4️⃣ COMFYUI SCHLIEßEN

```javascript
mcp__Control_your_Mac__osascript({
  script: 'quit app "ComfyUI"'
})
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
Timer IMMER mp4-Format!
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
    # Siehe arbeitsblatt-erstellen-v3 SKILL.md
```

### Für PowerPoints:
```python
def validate_presentation(pptx_path, expected_slides, expected_timers):
    # Prüft: Folienanzahl, Timer (mp4!), Umlaute
    # Siehe unterrichtsstunde-erstellen-v3 SKILL.md
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
| 4.0 | 24.01.2025 | v2-Skills, ComfyUI-Automation |
| **5.0** | **29.01.2026** | **v3-Skills, MCP-Tool-Namen (mcp__...), Timer mp4, SKILL-PFLICHT-CHECK** |
