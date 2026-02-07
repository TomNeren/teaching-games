# Quick-Start: Toms Skills integrieren

**Ziel:** Die wichtigsten Skills von Tom in 48h produktiv nutzen  
**Status:** Vorbereitet, bereit zur Implementierung

---

## 🎯 Phase 1: Foundation (Heute — 2h)

### 1. Methoden-Bibliothek kopieren

```bash
# Methoden-Bibliothek extrahieren und kopieren
cp teaching/tom-skills-extracted/methoden-bibliothek/methoden-bibliothek.md/methoden-bibliothek.md \
   teaching/methods-library.md

# Verifizieren
wc -l teaching/methods-library.md
# Sollte: 651 Zeilen sein
```

**Was haben wir jetzt?**
- 48 Unterrichtsmethoden mit detaillierten Durchführungshinweisen
- Kategorisiert: Einstieg (15), Erarbeitung (18), Sicherung (15)
- Einsatzbereit für Methodenwahl im Unterricht

---

### 2. H5P-Generator installieren

```bash
# Tool kopieren
cp teaching/tom-skills/h5p-generator/h5p_generator.py \
   teaching/tools/h5p_generator.py

chmod +x teaching/tools/h5p_generator.py

# Test
cd teaching/tools
python3 h5p_generator.py sample -o ./test-output

# Sollte erstellen:
# - sample_multichoice.h5p
# - sample_blanks.h5p
# - sample_flashcards.h5p
# - sample_truefalse.h5p
# - sample_quiz.h5p
```

**Was haben wir jetzt?**
- Interaktive H5P-Materialien programmatisch erstellen
- Multiple Choice, Fill-in-Blanks, Flashcards, True/False, Quizze
- Importierbar in Moodle, WordPress, H5P.com

---

### 3. Workflow-Prinzipien dokumentieren

```bash
# Template erstellen
cat > teaching/workflow-principles.md << 'EOF'
# Workflow-Prinzipien (von Tom)

## 6 Kernprinzipien

### 1. 🧵 Roter Faden (Story-Check)
Nach JEDER Stunde:
- Wie verbindet sich Einstieg mit Erarbeitung?
- Wie führt Erarbeitung zur Sicherung?
- Ist die Story konsistent?

### 2. 🔀 Hybrid Planung↔Ausführung
**Planung:** Kreativ, konzeptionell (Main Agent)
**Ausführung:** Technisch, materiell (Subagent/Workflow)

### 3. 📄 Textformat-Abfrage
Bei JEDER Textgenerierung fragen:
- Zeitungsartikel?
- Wissenschaftlicher Text?
- Argumentation?
- Dialog?

### 4. 📊 Sequentielle Stundenplanung
EINE Stunde vollständig durchdenken, dann nächste.
Nicht parallel planen!

### 5. 🖼️ Bildgenerierungs-Workflow
Prompt-Struktur: Subject → Action → Style → Technical

### 6. 🚨 Tool-Pflicht-Check
Bevor du von Grund auf neu baust:
- Gibt es ein existierendes Tool/Skill?
- Kann ich es anpassen statt neu zu bauen?

## Story-Check Template

```
🧵 STORY-CHECK Stunde {{NR}}:

1. EINSTIEG → Verbindung zu Erarbeitung 1: [Erklärung]
2. ERARBEITUNG 1 → Verbindung zu Erarbeitung 2: [Erklärung]
3. ERARBEITUNG 2 → Verbindung zu Sicherung: [Erklärung]
4. SICHERUNG → Verbindung zu Abschluss: [Erklärung]

❓ Ist diese Story konsistent? [Muss bestätigt werden!]
```

## Handover-Template (Planung → Ausführung)

```markdown
# Unterrichtsprojekt: {{PROJEKT_NAME}}

## Metadaten
| Feld | Wert |
|------|------|
| Projekt-ID | {{ID}} |
| Klasse | {{KLASSE}} |
| Fach | {{FACH}} |
| Dauer | {{STUNDEN}} Stunden |
| Datum | {{DATUM}} |

## Stunden-Übersicht
1. {{STUNDE_1_TITEL}}
2. {{STUNDE_2_TITEL}}
...

## Stunde 1: {{TITEL}}

### Roter Faden
[Story-Check Ergebnis hier]

### Phasen
**Einstieg ({{MIN}} Min):**
- Methode: {{METHODE}}
- Arbeitsauftrag: {{FERTIG GESCHRIEBENER TEXT}}
- Material: {{LISTE}}

**Erarbeitung 1 ({{MIN}} Min):**
...

### Materialien
- [ ] Arbeitsblatt "{{NAME}}" (.docx)
- [ ] Bild "{{NAME}}" (Prompt: "{{PROMPT}}")
- [ ] Audio "{{NAME}}" (falls Englisch)

### FERTIGE TEXTE
[Alle Arbeitsaufträge, AB-Inhalte, Texte VOLLSTÄNDIG hier]
```
EOF
```

**Was haben wir jetzt?**
- Strukturiertes Vorgehen für Unterrichtsplanung
- Story-Check Prozess
- Handover-System zwischen Planung und Ausführung

---

## 🎯 Phase 2: TTS-Workflow adaptieren (Morgen — 3h)

### 4. ElevenLabs Stimmen-Mapping

```bash
# ElevenLabs Voice Config erstellen
cat > teaching/tts-voices-elevenlabs.md << 'EOF'
# ElevenLabs Stimmen (analog zu Toms Kokoro)

## US English

### Female
- **Rachel** — Freundlich, warm (ähnlich Kokoro af_heart)
- **Domi** — Klar, artikuliert (ähnlich Kokoro af_sarah)
- **Bella** — Warm, beruhigend (ähnlich Kokoro af_bella)

### Male
- **Adam** — Neutral, professionell (ähnlich Kokoro am_michael)
- **Antoni** — Tief, autoritär (ähnlich Kokoro am_adam)
- **Sam** — Jung, modern (ähnlich Kokoro am_liam)

## British English

### Female
- **Charlotte** — Elegant, kultiviert (ähnlich Kokoro bf_emma)

### Male
- **George** — Klassisch, formell (ähnlich Kokoro bm_george)

## Verwendungsempfehlungen

| Aufgabentyp | ElevenLabs Stimme | OpenClaw Command |
|-------------|-------------------|------------------|
| Monolog/News | Adam | `tts "text" "Adam"` |
| Dialog Female | Rachel | `tts "text" "Rachel"` |
| Dialog Male | Antoni | `tts "text" "Antoni"` |
| UK Interview F | Charlotte | `tts "text" "Charlotte"` |
| UK Interview M | George | `tts "text" "George"` |
| Diktat | Domi | `tts "text" "Domi"` |

## Multi-Speaker Dialog (ffmpeg)

```bash
# Sprecher A generieren
tts "Good morning!" "Rachel" > speaker_a.mp3

# Sprecher B generieren
tts "Hello there!" "Adam" > speaker_b.mp3

# Mit Pausen zusammenfügen
ffmpeg -i speaker_a.mp3 -i speaker_b.mp3 \
  -filter_complex '[0:a][1:a]concat=n=2:v=0:a=1' \
  -f mp3 dialog.mp3
```

## Dateinamen-Konvention (von Tom)

```
[Klasse]_[Einheit]_Track[Nr]_[Beschreibung].mp3

Beispiele:
- AV3_Unit5_Track01_Introduction.mp3
- BTG2_NATO_Track01_CrisisBriefing.mp3
```

## Workflow

1. **Stimmauswahl** (obligatorisch!)
   ```
   🎤 STIMMAUSWAHL
   
   US Female: Rachel, Domi, Bella
   US Male: Adam, Antoni, Sam
   UK Female: Charlotte
   UK Male: George
   
   Welche Stimme(n)? → [User wählt]
   ```

2. **Audio generieren**
   ```bash
   tts "Your text here" "Rachel" > /path/to/archive/filename.mp3
   ```

3. **Archivieren**
   - Langzeit: `teaching/audio-archive/`
   - Projekt: `teaching/klassen/[KLASSE]/[PROJEKT]/audio/`

4. **Optional: Concat/Normalize**
   ```bash
   # Lautstärke normalisieren
   ffmpeg -i input.mp3 -filter:a loudnorm output.mp3
   ```
EOF
```

---

### 5. ffmpeg Audio-Helper erstellen

```bash
# Helper-Script erstellen
cat > teaching/tools/audio-helper.sh << 'EOF'
#!/bin/bash
# Audio Helper für Teaching

case "$1" in
  concat)
    # Mehrere Audio-Dateien mit Pausen zusammenfügen
    shift
    PAUSE_SEC=${PAUSE:-1}
    OUTPUT=${OUTPUT:-combined.mp3}
    
    echo "Concatenating with ${PAUSE_SEC}s pauses..."
    # Implementation hier
    ;;
    
  normalize)
    # Lautstärke normalisieren
    INPUT="$2"
    OUTPUT="${INPUT%.*}_normalized.mp3"
    ffmpeg -i "$INPUT" -filter:a loudnorm "$OUTPUT" -y
    echo "Normalized: $OUTPUT"
    ;;
    
  wav2mp3)
    # WAV zu MP3 konvertieren
    INPUT="$2"
    OUTPUT="${INPUT%.*}.mp3"
    ffmpeg -i "$INPUT" -codec:a libmp3lame -qscale:a 2 "$OUTPUT" -y
    echo "Converted: $OUTPUT"
    ;;
    
  *)
    echo "Usage: audio-helper.sh {concat|normalize|wav2mp3} [files...]"
    exit 1
    ;;
esac
EOF

chmod +x teaching/tools/audio-helper.sh
```

---

## 🎯 Phase 3: Bildgenerierung (Übermorgen — 2h)

### 6. Hugging Face Image API Helper

```bash
# Image Generator Helper
cat > teaching/tools/generate-image.sh << 'EOF'
#!/bin/bash
# Image Generator für Teaching (Hugging Face API)

PROMPT="$1"
OUTPUT="${2:-output.png}"
MODEL="${MODEL:-black-forest-labs/FLUX.1-schnell}"

# FLUX-Prompt-Struktur: Subject → Action → Style → Technical
# KEINE Quality Tags ("masterpiece", "8k")
# KEINE Künstlernamen

echo "Generating image with FLUX..."
echo "Prompt: $PROMPT"

# API Call hier (via curl oder OpenClaw tools)
# web_fetch + Hugging Face API

echo "Saved: $OUTPUT"
EOF

chmod +x teaching/tools/generate-image.sh
```

---

## ✅ Was haben wir nach 48h?

### Sofort nutzbar:
1. ✅ **Methoden-Bibliothek** (651 Zeilen, 48 Methoden)
2. ✅ **H5P-Generator** (Interaktive Materialien)
3. ✅ **Workflow-Prinzipien** (Story-Check, Sequentielle Planung)

### Nach 24h zusätzlich:
4. ✅ **TTS-Workflow** (ElevenLabs Mapping, Multi-Speaker)
5. ✅ **Audio-Helper** (ffmpeg concat, normalize)

### Nach 48h zusätzlich:
6. ✅ **Bildgenerierung** (Hugging Face API)

---

## 🚀 Nächste Verwendung

### Szenario: Englisch-Stunde mit Hörverstehen planen

```bash
# 1. Main Agent plant Stunde (mit Workflow-Prinzipien)
# → Story-Check
# → Methodenwahl aus methods-library.md
# → TTS-Stimmauswahl

# 2. Subagent erstellt Materialien
# → H5P Quiz generieren
# → Audio mit ElevenLabs
# → Bilder mit Hugging Face

# 3. Archivieren
# → Audio: teaching/audio-archive/AV3_Unit5_Track01.mp3
# → H5P: teaching/klassen/AV3/Unit5/materials/
```

---

## 📚 Referenzen

- **Vollständige Analyse:** `teaching/skills-analysis.md`
- **Rohdaten:** `teaching/tom-skills/` und `teaching/tom-skills-extracted/`
- **Toms Workflow v5+:** `teaching/tom-skills-extracted/workflow/unterrichtsplanung-workflow-v5+/`

---

*Stand: 03.02.2026*  
*Bereit zur Implementierung!*
