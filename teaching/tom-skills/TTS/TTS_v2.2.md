---
name: hoerverstehen-tts
description: Erstellt Audio-Dateien für Englisch-Hörverstehensaufgaben mit Kokoro (lokal, 28 EN Stimmen) oder Chatterbox (MCP, Voice Cloning). Nutze bei Anfragen nach Hörverstehen, Listening, Audio erstellen, Hörtext, Listening Comprehension, TTS, Text-to-Speech, Dialog-Audio oder Sprecher für Englisch-Unterricht.
---

# Hörverstehen TTS Skill v2.2

Generiert Audio für Listening Comprehension Aufgaben im Englischunterricht.

## When to Use This Skill

**Trigger-Wörter:**
- "Hörverstehen", "Listening", "Audio erstellen"
- "Hörtext", "Listening Comprehension"
- "Sprecher", "Dialog", "Conversation"
- "TTS", "Text-to-Speech"

**Nicht verwenden für:**
- Musik oder Soundeffekte
- Nicht-englische Sprachen (Skill ist EN-only)
- Stimmenimitation realer Personen (Copyright!)

---

## 📁 SPEICHERORTE

```
┌─────────────────────────────────────────────────────────────────┐
│  LANGZEIT-ARCHIV (iCloud-Sync, alle generierten Audios)        │
├─────────────────────────────────────────────────────────────────┤
│  ~/Library/Mobile Documents/com~apple~CloudDocs/               │
│    Schule/Material/TTS/Audio/Listening/                        │
│                                                                 │
│  Struktur:                                                      │
│  └── Listening/                                                 │
│      ├── 10a_Unit5_Track01_Introduction.wav                     │
│      └── AV3_LWK_Track01_Vorstellungsgespraech.wav              │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  ARBEITS-KOPIE (für aktuellen Unterricht)                      │
├─────────────────────────────────────────────────────────────────┤
│  ~/Library/Mobile Documents/com~apple~CloudDocs/               │
│    Schule/Unterricht/[KLASSE]/[EINHEIT]/Audio/                 │
│                                                                 │
│  Beispiel:                                                      │
│  └── AV3_EN/Unit_05/Audio/                                      │
│      └── Track01_Dialog.wav  ← Kopie aus Langzeit-Archiv       │
└─────────────────────────────────────────────────────────────────┘

WORKFLOW:
1. Audio generieren → Speichern in LANGZEIT-ARCHIV
2. Kopie erstellen → In ARBEITS-ORDNER der aktuellen Stunde
```

---

## ⚠️ PFLICHT: STIMMAUSWAHL VOR GENERIERUNG

**Bei JEDER Audio-Generierung MUSS dem Nutzer die Stimmauswahl angezeigt werden!**

```
┌─────────────────────────────────────────────────────────────────┐
│  🎤 STIMMAUSWAHL - Bitte wählen:                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  AMERICAN ENGLISH (lang_code='a')                               │
│  ──────────────────────────────────────────────────────────     │
│  FEMALE:                                                        │
│  • af_heart    - Freundlich, warm      ⭐ EMPFOHLEN Dialog      │
│  • af_sarah    - Klar, artikuliert     ⭐ EMPFOHLEN Diktat      │
│  • af_bella    - Warm, beruhigend                               │
│  • af_nicole   - Jung, natürlich                                │
│  • af_nova     - Energisch, lebhaft                             │
│  • af_sky      - Hell, jung                                     │
│                                                                 │
│  MALE:                                                          │
│  • am_michael  - Neutral, professionell ⭐ EMPFOHLEN News       │
│  • am_adam     - Tief, autoritär                                │
│  • am_eric     - Freundlich, warm                               │
│  • am_liam     - Jung, modern                                   │
│                                                                 │
│  BRITISH ENGLISH (lang_code='b')                                │
│  ──────────────────────────────────────────────────────────     │
│  FEMALE:                                                        │
│  • bf_emma     - Elegant, kultiviert   ⭐ EMPFOHLEN UK Female   │
│  • bf_isabella - Warm, freundlich                               │
│  • bf_lily     - Jung, modern                                   │
│                                                                 │
│  MALE:                                                          │
│  • bm_george   - Klassisch, formell    ⭐ EMPFOHLEN UK Male     │
│  • bm_lewis    - Modern, entspannt                              │
│  • bm_fable    - Erzählerisch                                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

Welche Stimme(n) soll ich verwenden?
```

---

## ⚡ TECHNISCHE LIMITS

### Kokoro Limits

| Parameter | Limit | Hinweis |
|-----------|-------|---------|
| **Max. Text pro Aufruf** | ~10.000 Zeichen | Pipeline chunked automatisch |
| **Empfohlen pro Aufruf** | ~3.000 Zeichen | Für beste Qualität |
| **Max. Audio-Dauer** | ~10 Minuten | Danach ggf. Speicherprobleme |

### Chatterbox Limits (MCP)

| Parameter | Limit | Hinweis |
|-----------|-------|---------|
| **Max. Text pro Aufruf** | 300 Zeichen | HART - muss gechunkt werden! |
| **Referenz-Audio** | 5-10 Sekunden | Für Voice Cloning |

---

## Verfügbare Tools

### 🥇 Kokoro (LOKAL - STANDARD)

**Setup:**
- Lokale Installation: ~/kokoro-tts (Python venv)
- Modell: Kokoro-82M (HuggingFace)
- Ausführung: Via Control your Mac:osascript

**Stärken:**
- ✅ 28 englische Stimmen (US & UK)
- ✅ Kostenlos & offline
- ✅ Schnelle Generierung
- ✅ Konsistente Qualität
- ✅ Automatisches Chunking (keine Längenbegrenzung)

**Einschränkungen:**
- ❌ Kein Voice Cloning
- ❌ Keine benutzerdefinierten Stimmen

---

### 🥈 Chatterbox (MCP - ERWEITERUNG)

**Verwendung:** Voice Cloning, bis zu 4 verschiedene Sprecher

**Tool:** Hugging Face:dynamic_space → ResembleAI/Chatterbox

**Stärken:**
- ✅ Zero-Shot Voice Cloning (5-10 Sek. Sample)
- ✅ Bis zu 4 verschiedene Sprecher
- ✅ Emotionale Tags ([laughs], [sighs], etc.)

**Einschränkungen:**
- ❌ Max. 300 Zeichen pro Anfrage (MUSS gechunkt werden!)
- ❌ Benötigt Referenz-Audio-URL
- ❌ Internetverbindung erforderlich

---

## Implementierung

### Kokoro: Einfache Generierung (KORRIGIERT v2.2)

**⚠️ WICHTIG:** Alle Chunks müssen gesammelt und kombiniert werden!

```javascript
Control your Mac:osascript({
  script: `do shell script "
    source ~/kokoro-tts/bin/activate && \\
    python3 << 'PYTHON'
from kokoro import KPipeline
import soundfile as sf
import numpy as np
import os

LANG = 'a'  # 'a' = American, 'b' = British
VOICE = 'af_heart'
TEXT = '''Your listening text here.'''
OUTPUT = os.path.expanduser('~/Library/Mobile Documents/com~apple~CloudDocs/Schule/Material/TTS/Audio/Listening/output.wav')

os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)

pipeline = KPipeline(lang_code=LANG)

# ✅ ALLE Chunks sammeln und kombinieren
all_audio = []
for _, _, audio in pipeline(TEXT, voice=VOICE):
    all_audio.append(audio)

combined = np.concatenate(all_audio)
sf.write(OUTPUT, combined, 24000)
print(f'Saved: {OUTPUT} ({len(all_audio)} chunks, {len(combined)/24000:.1f}s)')
PYTHON
  "`
})
```

### Kokoro: Dialog mit mehreren Sprechern

```javascript
Control your Mac:osascript({
  script: `do shell script "
    source ~/kokoro-tts/bin/activate && \\
    python3 << 'PYTHON'
from kokoro import KPipeline
import soundfile as sf
import numpy as np
import os

SPEAKERS = {
    'A': {'lang': 'b', 'voice': 'bf_emma'},
    'B': {'lang': 'a', 'voice': 'am_michael'},
}

DIALOG = [
    ('A', 'Good morning! How can I help you today?'),
    ('B', 'Hi, I would like to book a table for two.'),
]

all_audio = []
pause = np.zeros(int(24000 * 0.5))  # 0.5 Sekunden Pause

for speaker, text in DIALOG:
    cfg = SPEAKERS[speaker]
    pipeline = KPipeline(lang_code=cfg['lang'])
    # ✅ Alle Chunks pro Sprecher sammeln
    speaker_audio = []
    for _, _, audio in pipeline(text, voice=cfg['voice']):
        speaker_audio.append(audio)
    all_audio.append(np.concatenate(speaker_audio))
    all_audio.append(pause)

combined = np.concatenate(all_audio)
OUTPUT = os.path.expanduser('~/Library/Mobile Documents/com~apple~CloudDocs/Schule/Material/TTS/Audio/Listening/dialog.wav')
os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
sf.write(OUTPUT, combined, 24000)
print(f'Dialog saved! Duration: {len(combined)/24000:.1f}s')
PYTHON
  "`
})
```

### Kokoro: Langer Text mit Fortschrittsanzeige

Für sehr lange Texte (>3000 Zeichen) mit Fortschrittsinfo:

```javascript
Control your Mac:osascript({
  script: `do shell script "
    source ~/kokoro-tts/bin/activate && \\
    python3 << 'PYTHON'
from kokoro import KPipeline
import soundfile as sf
import numpy as np
import os

LANG = 'a'
VOICE = 'am_michael'
TEXT = '''[VERY LONG TEXT HERE - up to 10000 chars]'''
OUTPUT = os.path.expanduser('~/Library/Mobile Documents/com~apple~CloudDocs/Schule/Material/TTS/Audio/Listening/long_audio.wav')

os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)

pipeline = KPipeline(lang_code=LANG)

all_audio = []
chunk_count = 0

for _, _, audio in pipeline(TEXT, voice=VOICE):
    all_audio.append(audio)
    chunk_count += 1
    # Fortschritt ausgeben
    duration_so_far = sum(len(a) for a in all_audio) / 24000
    print(f'Chunk {chunk_count}: {duration_so_far:.1f}s total')

combined = np.concatenate(all_audio)
sf.write(OUTPUT, combined, 24000)
print(f'\\nComplete! {chunk_count} chunks, {len(combined)/24000:.1f}s total')
PYTHON
  "`
})
```

### Chatterbox: Voice Cloning (MCP) - Mit Chunking

**⚠️ WICHTIG:** Chatterbox hat ein 300-Zeichen-Limit! Text muss gechunkt werden.

```javascript
// Schritt 1: Text in Chunks aufteilen (max 300 Zeichen pro Chunk)
const text = "Your long text here...";
const chunks = [];
let current = "";
for (const sentence of text.split(/(?<=[.!?])\s+/)) {
  if ((current + sentence).length > 280) {
    chunks.push(current.trim());
    current = sentence;
  } else {
    current += " " + sentence;
  }
}
if (current.trim()) chunks.push(current.trim());

// Schritt 2: Jeden Chunk einzeln generieren
for (let i = 0; i < chunks.length; i++) {
  Hugging Face:dynamic_space({
    operation: "invoke",
    space_name: "ResembleAI/Chatterbox",
    parameters: JSON.stringify({
      text_input: chunks[i],
      audio_prompt_path_input: "https://cdn.openai.com/API/docs/audio/alloy.wav"
    })
  })
  // Download chunk_i.wav
}

// Schritt 3: Mit ffmpeg zusammenfügen (siehe unten)
```

### Arbeitskopie erstellen

```javascript
Control your Mac:osascript({
  script: 'do shell script "cp \\"$HOME/Library/Mobile Documents/com~apple~CloudDocs/Schule/Material/TTS/Audio/Listening/[DATEI].wav\\" \\"$HOME/Library/Mobile Documents/com~apple~CloudDocs/Schule/Unterricht/[KLASSE]/[EINHEIT]/Audio/\\""'
})
```

---

## Audio-Dateien zusammenführen (ffmpeg)

ffmpeg ist installiert unter /opt/homebrew/bin/ffmpeg.

### Mehrere Tracks mit Pause zusammenfügen

```javascript
Control your Mac:osascript({
  script: `do shell script "
    export PATH=/opt/homebrew/bin:\$PATH
    
    TRACK1='$HOME/Library/Mobile Documents/com~apple~CloudDocs/Schule/Material/TTS/Audio/Listening/track1.wav'
    TRACK2='$HOME/Library/Mobile Documents/com~apple~CloudDocs/Schule/Material/TTS/Audio/Listening/track2.wav'
    OUTPUT='$HOME/Library/Mobile Documents/com~apple~CloudDocs/Schule/Material/TTS/Audio/Listening/combined.wav'
    
    # 1 Sekunde Stille
    ffmpeg -f lavfi -i anullsrc=r=24000:cl=mono -t 1 -acodec pcm_s16le /tmp/silence.wav -y 2>/dev/null
    
    # Zusammenfügen
    ffmpeg -i \\"\$TRACK1\\" -i /tmp/silence.wav -i \\"\$TRACK2\\" \\
      -filter_complex '[0:a][1:a][2:a]concat=n=3:v=0:a=1[out]' \\
      -map '[out]' \\"\$OUTPUT\\" -y 2>/dev/null
    
    echo 'Combined!'
  "`
})
```

### Lautstärke normalisieren

```javascript
Control your Mac:osascript({
  script: 'do shell script "export PATH=/opt/homebrew/bin:\$PATH && ffmpeg -i input.wav -filter:a loudnorm output.wav -y 2>/dev/null"'
})
```

### WAV zu MP3 konvertieren

```javascript
Control your Mac:osascript({
  script: 'do shell script "export PATH=/opt/homebrew/bin:\$PATH && ffmpeg -i input.wav -codec:a libmp3lame -qscale:a 2 output.mp3 -y 2>/dev/null"'
})
```

---

## Dateinamen-Konvention

```
[Klasse]_[Einheit]_Track[Nr]_[Beschreibung].wav

Beispiele:
├── 10a_Unit5_Track01_Introduction.wav
├── 10a_Unit5_Track02_DialogRestaurant.wav
├── BTG2_NATO_Track01_CrisisBriefing.wav
└── AV3_LWK_Track01_Bewerbung.wav
```

---

## Empfehlungen nach Aufgabentyp

| Aufgabentyp | Tool | Stimme(n) | Max. Länge |
|-------------|------|-----------|------------|
| Monolog/News | Kokoro | am_michael, am_adam | ~10 Min |
| Dialog (2 Personen) | Kokoro | af_heart + am_michael | ~10 Min |
| UK Interview | Kokoro | bf_emma + bm_george | ~10 Min |
| Diktat | Kokoro | af_sarah | ~5 Min |
| Storytelling | Kokoro | bm_fable | ~10 Min |
| Voice Clone | Chatterbox | Custom | ~2 Min (wg. Chunking) |

---

## Checkliste

- [ ] Stimmauswahl dem Nutzer angezeigt
- [ ] Stimme gewählt und bestätigt
- [ ] Text vorbereitet (keine Abkürzungen, Zahlen ausgeschrieben)
- [ ] Textlänge geprüft (Kokoro: ~3000 Zeichen optimal, Chatterbox: max 300!)
- [ ] Audio generiert (mit korrektem Chunk-Handling!)
- [ ] Im Langzeit-Archiv gespeichert
- [ ] Arbeitskopie in Projekt-Ordner erstellt
- [ ] Audio angehört und geprüft

---

## Troubleshooting

### Problem: Audio ist abgeschnitten
**Ursache:** Alter Code mit `break` nach erstem Chunk
**Lösung:** Neuen Code mit `all_audio.append()` und `np.concatenate()` verwenden

### Problem: Chatterbox gibt Fehler
**Ursache:** Text > 300 Zeichen
**Lösung:** Text in Sätze aufteilen, jeden Satz einzeln generieren, dann mit ffmpeg zusammenfügen

### Problem: Stimme klingt unnatürlich bei langen Pausen
**Ursache:** Zu lange Pause zwischen Chunks
**Lösung:** Pause auf 0.3-0.5 Sekunden reduzieren: `pause = np.zeros(int(24000 * 0.3))`

---

## Changelog

| Version | Datum | Änderungen |
|---------|-------|------------|
| 2.2.0 | 28.01.2026 | **BUGFIX:** Chunk-Handling korrigiert (alle Chunks sammeln statt break), Limits dokumentiert, Troubleshooting ergänzt |
| 2.1.0 | 27.01.2026 | Stimmauswahl-Pflicht, ffmpeg-Integration, Pfad-Konzept |
| 2.0.0 | 27.01.2026 | Korrektes MCP-Format, 28 EN Stimmen |
| 1.0.0 | 27.01.2026 | Initial Release |

---

*Version: 2.2.0*
*Abhängigkeiten: Kokoro (lokal), Chatterbox (HuggingFace MCP), ffmpeg*
