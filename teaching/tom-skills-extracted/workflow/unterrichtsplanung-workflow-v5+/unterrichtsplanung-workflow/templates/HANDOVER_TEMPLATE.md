# HANDOVER_TEMPLATE für Claude Cowork

**Version:** 5.0 (29.01.2026)
**Workflow:** Unified Lesson Planning mit 6 Kernprinzipien
**Referenz-Skill:** `/mnt/skills/user/unterrichtsplanung-workflow/SKILL.md`

---

## ⚡ Anweisung an Claude Cowork

> **WICHTIG:** Lies zuerst alle relevanten Skills unter `/mnt/skills/user/`
> **v5.0:** Verwende die v3-Skills (arbeitsblatt-erstellen-v3, unterrichtsstunde-erstellen-v3)

---

## 🚨 SKILL-PFLICHT-CHECK (IMMER ZUERST!)

```
┌─────────────────────────────────────────────────────────────────────────┐
│  Welche Datei soll erstellt werden?                                     │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  .docx für Unterricht?                                                  │
│  → arbeitsblatt-erstellen-v3 PFLICHT!                                   │
│  → Auch für: Infoblätter, Country Profiles, Crisis Briefings            │
│                                                                         │
│  .pptx für Unterricht?                                                  │
│  → unterrichtsstunde-erstellen-v3 PFLICHT!                              │
│  → Auch für: Simulationen, Multi-Session PPTs, Workshop Slides          │
│                                                                         │
│  Bilder für Unterricht?                                                 │
│  → unterrichts-medien PFLICHT!                                          │
│  → ComfyUI → nanobanana → Hugging Face                                  │
│                                                                         │
│  ⚠️ NIEMALS eigene Scripts von Grund auf erstellen wenn Skill           │
│     mit Vorlage verfügbar ist!                                          │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Skill-Routing (v3 Skills!)

### Für alle Fächer:

```
1. ARBEITSBLÄTTER ERSTELLEN
   → Skill: /mnt/skills/user/arbeitsblatt-erstellen-v3/SKILL.md
   → Vorlage AB: /mnt/skills/user/arbeitsblatt-erstellen-v3/templates/Vorlage_Fach.docx
   → Vorlage KA: /mnt/skills/user/arbeitsblatt-erstellen-v3/templates/Vorlage_Klassenarbeit.docx

2. BILDER GENERIEREN (mit ComfyUI-Automation)
   → Skill: /mnt/skills/user/unterrichts-medien/SKILL.md
   → Primär: mcp__comfyui__generate_image
   → Fallback 1: mcp__nanobanana__generate_image
   → Fallback 2: mcp__fa86031e-8beb-4aac-b517-e3b796ddf8ec__gr4_z_image_turbo_generate
   → Format: 16:9 (1024x576 oder 1280x720)

3. POWERPOINT ERSTELLEN
   → Skill: /mnt/skills/user/unterrichtsstunde-erstellen-v3/SKILL.md
   → Vorlage: /mnt/skills/user/unterrichtsstunde-erstellen-v3/Vorlage.pptx
   → Timer: IMMER mp4 aus Timer-Ordner

4. VOKABELLISTE ERSTELLEN (nur Englisch!)
   → Skill: /mnt/skills/user/vokabeln-zusammenfassen/SKILL.md
   → Format: B2+, Word Families, AWL-Prüfung
   → WICHTIG: Erst NACH Materialien erstellen (aus fertigen Texten extrahieren)

5. SELF-ASSESSMENT ERSTELLEN
   → Template DE: /mnt/skills/user/unterrichtsplanung-workflow/templates/SELF_ASSESSMENT_DE.md
   → Template EN: /mnt/skills/user/unterrichtsplanung-workflow/templates/SELF_ASSESSMENT_EN.md
   → Format: Teil A (4-6 Inhaltsfragen) + Teil B-D (Reflexion)

6. OUTPUT-ORDNER (iCloud-Struktur) → siehe unten
```

---

## ⏱️ Timer-System (IMMER mp4!)

### Timer-Ordner (ALLE Timer hier!)

```
/Users/tomren/Library/CloudStorage/GoogleDrive-renne.tom@googlemail.com/Meine Ablage/Claude-Meta-Projekt/ppt_update/timer_pixel_schnee/
```

### Verfügbare Timer (mp4)

| Dauer | Dateiname |
|-------|-----------|
| 3 min | `timer_pixel_3min.mp4` |
| 4 min | `timer_pixel_4min.mp4` |
| 5 min | `timer_pixel_5min.mp4` |
| 6 min | `timer_pixel_6min.mp4` |
| 7 min | `timer_pixel_7min.mp4` |
| 8 min | `timer_pixel_8min.mp4` |
| 9 min | `timer_pixel_9min.mp4` |
| 10 min | `timer_pixel_10min.mp4` |
| 12 min | `timer_pixel_12min.mp4` |
| 15 min | `timer_pixel_15min.mp4` |
| 20 min | `timer_pixel_20min.mp4` |
| 25 min | `timer_pixel_25min.mp4` |
| 30 min | `timer_pixel_30min.mp4` |

### Timer-Position auf Folien

- **Y-Position:** 13.8-13.9 Zoll vom oberen Rand
- **Breite:** Volle Folienbreite (26.67")
- **Arbeitsauftrag:** IMMER OBEN (nicht unten!)

---

## 📁 iCloud-Ordnerstruktur

### Basis-Pfad:

```
/Users/tomren/Library/Mobile Documents/com~apple~CloudDocs/Schule/Unterricht/MPS/2025:26_HJ2/
```

### Struktur:

```
[Klasse]/                              # z.B. AV3_LWK, EG2, BKSP_E_FH_1
└── [Einheit_oder_Thema]/              # z.B. BPE1_Berufsvorbereitung
    ├── Stunde_01/
    │   ├── doc/
    │   │   ├── AB_01_[Titel].docx
    │   │   ├── AB_01_[Titel]_NiveauA.docx    (falls differenziert)
    │   │   └── VocabSheet_01.docx            (nur Englisch)
    │   └── Stunde_01_PPT.pptx
    ├── Stunde_02/
    │   ├── doc/
    │   │   └── AB_02_[Titel].docx
    │   └── Stunde_02_PPT.pptx
    └── Self_Assessment_[Einheit].docx

Medien/                                # ZENTRAL für alle Klassen
├── Illustrationen/
├── Infografiken/
├── Icons/
└── Fotos/
```

### Dateinamen-Konventionen

| Typ | Format | Beispiel |
|-----|--------|----------|
| Arbeitsblatt | `AB_[Nr]_[Titel].docx` | `AB_01_Staerkenanalyse.docx` |
| AB differenziert | `AB_[Nr]_[Titel]_Niveau[A/B/C].docx` | `AB_01_Staerkenanalyse_NiveauA.docx` |
| Vokabelliste | `VocabSheet_[Nr].docx` | `VocabSheet_01.docx` |
| PowerPoint | `Stunde_[Nr]_PPT.pptx` | `Stunde_01_PPT.pptx` |
| Self-Assessment | `Self_Assessment_[Einheit].docx` | `Self_Assessment_BPE1.docx` |
| Bilder | `[beschreibung]_[nr].webp` | `chirurg_op_01.webp` |

---

## 🖼️ ComfyUI Bild-Workflow (mit Bild-Transfer)

### Schritt 1: ComfyUI Status prüfen

```javascript
mcp__Control_your_Mac__osascript({
  script: 'do shell script "curl -s -m 5 http://127.0.0.1:8188/system_stats"'
})
```

### Schritt 2: ComfyUI starten (falls nicht läuft)

```javascript
mcp__Control_your_Mac__osascript({
  script: 'do shell script "cd ~/ComfyUI && source venv/bin/activate && python main.py --use-pytorch-cross-attention --force-fp16 &> /tmp/comfyui.log &\necho started"'
})
```

### Schritt 3: Warten (8 Sekunden)

```javascript
mcp__Control_your_Mac__osascript({
  script: 'delay 8'
})
```

### Schritt 4: Bild generieren

```javascript
mcp__comfyui__generate_image({
  prompt: "{{PROMPT}}",
  width: 1024,
  height: 576,  // 16:9 für PPTX
  seed: -1
})
```

### Schritt 5: Bild-Transfer (Cowork → iCloud)

Nach erfolgreicher Generierung wird das Bild automatisch im Output-Ordner gespeichert.

**Für manuelle Transfers (falls nötig):**

```javascript
// Via Desktop Commander (auf Host)
mcp__Control_your_Mac__osascript({
  script: 'do shell script "curl -sL \\"{{HF_URL}}\\" -o \\"{{ZIEL_PFAD}}\\""'
})
```

### Schritt 6: ComfyUI schließen (nach allen Bildern)

```javascript
mcp__Control_your_Mac__osascript({
  script: 'quit app "ComfyUI"'
})
```

### Fallback-Kaskade (bei ComfyUI-Fehler)

```
1. mcp__comfyui__generate_image (lokal, schnell)
   ↓ Bei Fehler
2. mcp__nanobanana__generate_image (Google Gemini)
   ↓ Bei Fehler
3. mcp__fa86031e-8beb-4aac-b517-e3b796ddf8ec__gr4_z_image_turbo_generate (HuggingFace)
```

---

## 📝 Self-Assessment Struktur

### Teil A: Inhaltsfragen (4-6 Fragen)
- Beziehen sich auf konkrete Lerninhalte der Stunde/Einheit
- Überprüfen Verständnis der Kernkonzepte

### Teil B: Selbsteinschätzung
- Skala 1-5 oder Smileys
- "Ich kann jetzt..." / "Ich verstehe..."

### Teil C: Lernstrategien
- "Was hat mir beim Lernen geholfen?"
- "Was war schwierig?"

### Teil D: Ziele
- "Das möchte ich noch üben..."
- "Mein nächster Schritt..."

---

## Skill-Referenzen (v3!)

| Skill | Pfad | Funktion |
|-------|------|----------|
| arbeitsblatt-erstellen-v3 | `/mnt/skills/user/arbeitsblatt-erstellen-v3/` | ALLE .docx für Unterricht |
| unterrichtsstunde-erstellen-v3 | `/mnt/skills/user/unterrichtsstunde-erstellen-v3/` | ALLE .pptx für Unterricht |
| unterrichts-medien | `/mnt/skills/user/unterrichts-medien/` | Bildgenerierung (ComfyUI) |
| methoden-bibliothek | `/mnt/skills/user/methoden-bibliothek/` | 48 Unterrichtsmethoden |
| vokabeln-zusammenfassen | `/mnt/skills/user/vokabeln-zusammenfassen/` | Vokabellisten (Englisch) |
| unterrichtsplanung-workflow | `/mnt/skills/user/unterrichtsplanung-workflow/` | Dieser Workflow |

---

## Differenzierung

| Niveau | Anpassung |
|--------|-----------|
| A | Lückentexte, Wortbanken, Bilder, Hilfen |
| B | Standard, offenere Aufgaben |
| C | Komplexe Texte, weniger Scaffolding |

---

# 📋 Handover-Vorlage (zum Ausfüllen)

```markdown
# Übergabeprotokoll: {{EINHEIT_TITEL}}

## Metadaten

| Feld | Wert |
|------|------|
| **Projekt-ID** | {{KLASSE}}_{{EINHEIT}}_{{DATUM}} |
| **Klasse** | {{KLASSE}} |
| **Fach** | {{FACH}} |
| **Stunde(n)** | {{ANZAHL}} × {{DAUER}} Min |
| **Niveau** | {{NIVEAU_BEREICH}} |
| **Ausstattung** | Beamer, iPads (1:2), Tafel |
| **Besonderheiten** | {{BESONDERHEITEN}} |

---

## PFLICHT-SKILLS FÜR DIESE EINHEIT

| Dateityp | Skill | Vorlage/Tool |
|----------|-------|--------------|
| .docx | arbeitsblatt-erstellen-v3 | Vorlage_Fach.docx |
| .pptx | unterrichtsstunde-erstellen-v3 | Vorlage.pptx |
| Bilder | unterrichts-medien | mcp__comfyui__generate_image |
| Timer | - | /Users/tomren/.../timer_pixel_schnee/ |

⚠️ NIEMALS eigene Scripts von Grund auf erstellen!
⚠️ IMMER zuerst die Skills lesen und Vorlagen laden!

---

## Stundenübersicht

| Stunde | Thema | Lernziele | Produkte |
|--------|-------|-----------|----------|
| 1 | {{THEMA_1}} | {{LERNZIELE_1}} | AB_01, PPT |
| 2 | {{THEMA_2}} | {{LERNZIELE_2}} | AB_02, PPT |

---

## 🧵 Story-Check (aus Chat-Planung)

### Stunde 1: {{THEMA}}

```
1. EINSTIEG → Erarbeitung 1: {{VERBINDUNG_1}}
2. ERARBEITUNG 1 → Erarbeitung 2: {{VERBINDUNG_2}}
3. ERARBEITUNG 2 → Sicherung: {{VERBINDUNG_3}}
4. SICHERUNG → Abschluss: {{VERBINDUNG_4}}

✅ Story-Check bestätigt: [Ja/Nein]
```

---

## Stunde {{NR}}: {{THEMA}}

### Lernziele (max. 60 Zeichen pro Zeile!)

- {{LERNZIEL_1}}
- {{LERNZIEL_2}}
- {{LERNZIEL_3}}

### Ablauf

| Phase | Zeit | Methode | Beschreibung | Material |
|-------|------|---------|--------------|----------|
| Einstieg | {{ZEIT}} | {{METHODE}} | {{BESCHREIBUNG}} | {{MATERIAL_ID}} |
| Erarbeitung | {{ZEIT}} | {{METHODE}} | {{BESCHREIBUNG}} | {{MATERIAL_ID}} |
| Sicherung | {{ZEIT}} | {{METHODE}} | {{BESCHREIBUNG}} | {{MATERIAL_ID}} |
| Abschluss | {{ZEIT}} | {{METHODE}} | {{BESCHREIBUNG}} | — |

### Timer-Bedarf (IMMER mp4!)

| Phase | Dauer | Timer-Datei | Arbeitsauftrag |
|-------|-------|-------------|----------------|
| {{PHASE}} | {{MIN}} Min | timer_pixel_{{MIN}}min.mp4 | {{VOLLSTÄNDIGER_ARBEITSAUFTRAG}} |

---

## Material-Checkliste

| ID | Material | Differenzierung | Status |
|----|----------|-----------------|--------|
| AB_01 | {{TITEL}} | Standard | [ ] |
| AB_01a | {{TITEL}} (vereinfacht) | Niveau A | [ ] |
| IMG_01 | {{BILD_BESCHREIBUNG}} | — | [ ] |
| PPT_01 | Präsentation Stunde 1 | — | [ ] |
| VS_01 | VocabSheet (nur EN) | — | [ ] |
| SA_01 | Self-Assessment | — | [ ] |

---

## Bild-Prompts (für ComfyUI/Fallback)

| ID | Prompt | Format |
|----|--------|--------|
| IMG_01 | "{{PROMPT}}" | 16:9 (1024x576), educational, high contrast |
| IMG_02 | "{{PROMPT}}" | {{FORMAT}} |

---

## AB-Inhalte (VOLLSTÄNDIG AUSFORMULIERT!)

### AB_01: {{TITEL}}

**Arbeitsblatt-Kopf (Platzhalter → Werte):**
| Platzhalter | Wert |
|-------------|------|
| `[Thema]` | {{THEMA}} |
| `[Fach]` | {{FACH}} |
| `[Ziel 1 – nicht länger als eine Zeile]` | {{ZIEL_1}} |
| `[Ziel 2 – nicht länger als eine Zeile]` | {{ZIEL_2}} |
| `[Ziel 3 – nicht länger als eine Zeile]` | {{ZIEL_3}} |
| `[A / B / C]` | {{NIVEAU}} |

**Body-Inhalt (FERTIG AUSFORMULIERT!):**

#### Aufgabe 1: {{TITEL}}

{{VOLLSTÄNDIGER_AUFGABENTEXT}}

#### Aufgabe 2: {{TITEL}}

{{VOLLSTÄNDIGER_AUFGABENTEXT}}

---

## PowerPoint-Struktur

### PPT Stunde {{NR}}

| Folie | Layout (Index) | Inhalt |
|-------|----------------|--------|
| 1 | 0 (Titel) | {{LEHRKRAFT}}, {{FACH}}, {{THEMA}} |
| 2 | 3 (Titel & Punkte) | Ablauf mit Zeiten |
| 3 | 3 (Titel & Punkte) | Lernziele (3 Bullets) |
| 4 | 5 (Timer-Folie) | Arbeitsauftrag + {{MIN}} Min Timer (mp4!) |
| 5 | 7 (Abschnitt) | Phasenwechsel |
| ... | ... | ... |

---

## Self-Assessment Inhaltsfragen

1. {{INHALTSFRAGE_1}}
2. {{INHALTSFRAGE_2}}
3. {{INHALTSFRAGE_3}}
4. {{INHALTSFRAGE_4}}

---

## Erfolgskriterien

- [ ] Alle Arbeitsblätter erstellt und validiert
- [ ] Differenzierungsstufen vorhanden (wenn nötig)
- [ ] Bilder generiert und in Materialien eingefügt
- [ ] PowerPoint hat Timer-Videos (mp4!) mit Arbeitsaufträgen OBEN
- [ ] Self-Assessment fachlich korrekt
- [ ] Vokabelliste erstellt (nur Englisch)
- [ ] Dateien in korrekter iCloud-Struktur gespeichert
- [ ] Dateinamen folgen Konvention
- [ ] ALLE Platzhalter ersetzt (keine [...] mehr!)
- [ ] Umlaute korrekt (ä/ö/ü/ß)

---

*Protokoll erstellt: {{DATUM}}*
*Status: Bereit für Materialerstellung*
```

---

## Zweiter Output: methoden-historie-update.md

Am Ende der Planung ZUSÄTZLICH erstellen:

```markdown
# Methoden-Historie Update

**Projekt:** {{PROJEKT_ID}}
**Datum:** {{DATUM}}

## Neue Einträge (zum Einfügen in methoden-historie.md)

| Datum | Stunde/Thema | Einstieg | Erarbeitung | Sicherung |
|-------|--------------|----------|-------------|-----------|
| {{DATUM}} | {{THEMA_1}} | {{METHODE_E1}} | {{METHODE_ER1}} | {{METHODE_S1}} |
| {{DATUM}} | {{THEMA_2}} | {{METHODE_E2}} | {{METHODE_ER2}} | {{METHODE_S2}} |

## Variationswarnungen (aktualisiert)

- {{METHODE_X}} ({{ANZAHL}}x) → ⚠️/🔴

## Anweisung

Bitte diese Einträge in die methoden-historie.md im Project Knowledge einfügen.
```

---

## Version History

| Version | Datum | Änderungen |
|---------|-------|------------|
| 1.0 | 17.01.2025 | Initiale Erstellung |
| 2.0 | 18.01.2025 | iCloud-Struktur hinzugefügt |
| 3.0 | 18.01.2025 | Unified Version mit Skill-Referenzen |
| 4.0 | 24.01.2025 | v2-Skills, ComfyUI-Automation, Story-Check |
| **5.0** | **29.01.2026** | **v3-Skills, MCP-Tool-Namen vereinheitlicht (mcp__...), Timer IMMER mp4, Bild-Transfer-Workflow, SKILL-PFLICHT-CHECK** |
