# HANDOVER_TEMPLATE für Claude Cowork

**Version:** 4.0 (24.01.2025)
**Workflow:** Unified Lesson Planning mit 5 Kernprinzipien
**Referenz-Skill:** `/mnt/skills/user/unterrichtsplanung-workflow/SKILL.md`

---

## ⚡ Anweisung an Claude Cowork

> **WICHTIG:** Lies zuerst alle relevanten Skills unter `/mnt/skills/user/`
> **NEU in v4:** Verwende die v2-Skills (arbeitsblatt-erstellen-v2, unterrichtsstunde-erstellen-v2)

---

## Skill-Routing (v2 Skills!)

### Für Englisch-Stunden:

```
1. ARBEITSBLÄTTER ERSTELLEN
   → Skill: /mnt/skills/user/arbeitsblatt-erstellen-v2/SKILL.md
   → Vorlage AB: /mnt/skills/user/arbeitsblatt-erstellen-v2/templates/Vorlage_Fach.docx
   → Vorlage KA: /mnt/skills/user/arbeitsblatt-erstellen-v2/templates/Vorlage_Klassenarbeit.docx

2. BILDER GENERIEREN (mit ComfyUI-Automation)
   → Primär: ComfyUI (comfyui:generate_image)
   → Fallback 1: nanobanana:generate_image
   → Fallback 2: Hugging Face gr4_z_image_turbo_generate
   → Format: 16:9 (1280x720)

3. POWERPOINT ERSTELLEN
   → Skill: /mnt/skills/user/unterrichtsstunde-erstellen-v2/SKILL.md
   → Vorlage: /mnt/skills/user/unterrichtsstunde-erstellen-v2/Vorlage.pptx
   → Timer intern: 4, 5, 10 min
   → Timer extern: 3, 6, 7, 8, 9, 12, 15, 20, 25, 30 min
   → Externer Timer-Pfad: /Users/tomren/.../Claude-Meta-Projekt/ppt_update/timer_pixel_schnee/

4. VOKABELLISTE ERSTELLEN (nur Englisch!)
   → Skill: /mnt/skills/user/vokabeln-zusammenfassen/SKILL.md
   → Format: B2+, Word Families, AWL-Prüfung
   → WICHTIG: Erst NACH Materialien erstellen (aus fertigen Texten extrahieren)

5. SELF-ASSESSMENT ERSTELLEN
   → Format: Teil A (4-6 Inhaltsfragen) + Teil B-D (Reflexion)
   → Sprache: Englisch

6. OUTPUT-ORDNER (iCloud-Struktur) → siehe unten
```

### Für andere Fächer (GGK, LWK, etc.):

```
1. ARBEITSBLÄTTER ERSTELLEN
   → Skill: /mnt/skills/user/arbeitsblatt-erstellen-v2/SKILL.md
   → Vorlagen wie oben

2. BILDER GENERIEREN (mit ComfyUI-Automation)
   → Wie oben

3. POWERPOINT ERSTELLEN
   → Skill: /mnt/skills/user/unterrichtsstunde-erstellen-v2/SKILL.md
   → Wie oben

4. SELF-ASSESSMENT ERSTELLEN
   → Format: Teil A (4-6 Inhaltsfragen) + Teil B-D (Reflexion)
   → Sprache: Deutsch

5. OUTPUT-ORDNER (iCloud-Struktur) → siehe unten
```

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

## ⏱️ Timer-System (v2)

### Im Skill enthalten (häufig genutzt)

| Dauer | Pfad |
|-------|------|
| 4 min | `/mnt/skills/user/unterrichtsstunde-erstellen-v2/timer/timer_pixel_4min.mp4` |
| 5 min | `/mnt/skills/user/unterrichtsstunde-erstellen-v2/timer/timer_pixel_5min.mp4` |
| 10 min | `/mnt/skills/user/unterrichtsstunde-erstellen-v2/timer/timer_pixel_10min.mp4` |

### Extern verfügbar (bei Bedarf laden)

| Dauer | Pfad |
|-------|------|
| 3, 6-9, 12, 15, 20, 25, 30 min | `/Users/tomren/.../Claude-Meta-Projekt/ppt_update/timer_pixel_schnee/timer_pixel_Xmin.mp4` |

### Timer-Position auf Folien

- **Y-Position:** 13.8-13.9 Zoll vom oberen Rand
- **Breite:** Volle Folienbreite (26.67")
- **Arbeitsauftrag:** IMMER OBEN (nicht unten!)

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

## 🖼️ ComfyUI Bild-Workflow

```bash
# 1. ComfyUI starten
open -a "ComfyUI"

# 2. Warten bis Server bereit (wichtig!)
until curl -s http://127.0.0.1:8188 > /dev/null; do
    sleep 2
done

# 3. Pro Bild generieren
comfyui:generate_image
  prompt: "{{PROMPT}}"
  width: 1280
  height: 720
  
# 4. Nach allen Bildern: ComfyUI schließen
osascript -e 'quit app "ComfyUI"'
```

**Fallback bei Fehler:**
1. nanobanana:generate_image (Gemini-basiert)
2. Hugging Face gr4_z_image_turbo_generate

---

## Skill-Referenzen (v2!)

| Skill | Pfad | Funktion |
|-------|------|----------|
| arbeitsblatt-erstellen-v2 | `/mnt/skills/user/arbeitsblatt-erstellen-v2/` | .docx mit bereinigten Vorlagen |
| unterrichtsstunde-erstellen-v2 | `/mnt/skills/user/unterrichtsstunde-erstellen-v2/` | .pptx mit Video-Timern |
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
| **Skill-Routing** | Englisch / Andere Fächer |

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

### Timer-Bedarf

| Phase | Dauer | Arbeitsauftrag (VOLLSTÄNDIG AUSFORMULIERT!) |
|-------|-------|---------------------------------------------|
| {{PHASE}} | {{MIN}} Min | {{VOLLSTÄNDIGER_ARBEITSAUFTRAG}} |

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
| IMG_01 | "{{PROMPT}}" | 16:9, cartoon, educational |
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
| 4 | 5 (Timer-Folie) | Arbeitsauftrag + {{MIN}} Min Timer |
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
- [ ] PowerPoint hat Timer-Videos mit Arbeitsaufträgen OBEN
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

- v1.0 (17.01.2025): Initiale Erstellung
- v2.0 (18.01.2025): iCloud-Struktur hinzugefügt
- v3.0 (18.01.2025): Unified Version mit Skill-Referenzen
- **v4.0 (24.01.2025): v2-Skills, ComfyUI-Automation, Story-Check, vollständige Texte im Handover, methoden-historie-update**
