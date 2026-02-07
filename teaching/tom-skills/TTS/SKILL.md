---
name: hoerverstehen-tts
version: 2.1.0
description: Erstellt Audio-Dateien für Englisch-Hörverstehensaufgaben. Nutzt Kokoro (lokal, 28 EN Stimmen) als Standard und Chatterbox (MCP, Voice Cloning) als Erweiterung für spezielle Anforderungen.
---

# Hörverstehen TTS Skill

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
- ❌ Max. 300 Zeichen pro Anfrage
- ❌ Benötigt Referenz-Audio-URL
- ❌ Internetverbindung erforderlich

---

## Implementierung

### Kokoro: Einfache Generierung

```javascript
Control your Mac:osascript({
  script: \`do shell script "
    source ~/kokoro-tts/bin/activate && \\
    python3 << 'PYTHON'
from kokoro import KPipeline
import soundfile as sf
import os

LANG = 'a'  # 'a' = American, 'b' = British
VOICE = 'af_heart'
TEXT = '''Your listening text here.'''
OUTPUT = os.path.expanduser('~/Library/Mobile Documents/com~apple~CloudDocs/Schule/Material/TTS/Audio/Listening/output.wav')

pipeline = KPipeline(lang_code=LANG)
for _, _, audio in pipeline(TEXT, voice=VOICE):
    sf.write(OUTPUT, audio, 24000)
    print(f'Saved: {OUTPUT}')
    break
PYTHON
  "\`
})
```

### Kokoro: Dialog mit mehreren Sprechern

```javascript
Control your Mac:osascript({
  script: \`do shell script "
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
pause = np.zeros(int(24000 * 0.5))

for speaker, text in DIALOG:
    cfg = SPEAKERS[speaker]
    pipeline = KPipeline(lang_code=cfg['lang'])
    for _, _, audio in pipeline(text, voice=cfg['voice']):
        all_audio.append(audio)
        all_audio.append(pause)
        break

combined = np.concatenate(all_audio)
OUTPUT = os.path.expanduser('~/Library/Mobile Documents/com~apple~CloudDocs/Schule/Material/TTS/Audio/Listening/dialog.wav')
sf.write(OUTPUT, combined, 24000)
print('Dialog saved!')
PYTHON
  "\`
})
```

### Chatterbox: Voice Cloning (MCP)

```javascript
// 1. Audio generieren
Hugging Face:dynamic_space({
  operation: "invoke",
  space_name: "ResembleAI/Chatterbox",
  parameters: JSON.stringify({
    text_input: "Your text here.",
    audio_prompt_path_input: "https://cdn.openai.com/API/docs/audio/alloy.wav"
  })
})

// 2. Download via osascript
Control your Mac:osascript({
  script: 'do shell script "curl -L \\"[AUDIO_URL]\\" -o \\"$HOME/Library/Mobile Documents/com~apple~CloudDocs/Schule/Material/TTS/Audio/Listening/cloned.wav\\""'
})
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
  script: \`do shell script "
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
  "\`
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
└── AV3_LWK_Track01_Bewerbung.wav
```

---

## Empfehlungen nach Aufgabentyp

| Aufgabentyp | Tool | Stimme(n) |
|-------------|------|-----------|
| Monolog | Kokoro | am_michael |
| Dialog (2) | Kokoro | af_heart + am_michael |
| UK Interview | Kokoro | bf_emma + bm_george |
| Diktat | Kokoro | af_sarah |
| Storytelling | Kokoro | bm_fable |
| Voice Clone | Chatterbox | Custom |

---

## Checkliste

- [ ] Stimmauswahl dem Nutzer angezeigt
- [ ] Stimme gewählt und bestätigt
- [ ] Text vorbereitet (keine Abkürzungen)
- [ ] Audio generiert
- [ ] Im Langzeit-Archiv gespeichert
- [ ] Arbeitskopie in Projekt-Ordner erstellt
- [ ] Audio angehört und geprüft

---

## Changelog

| Version | Datum | Änderungen |
|---------|-------|------------|
| 2.1.0 | 27.01.2026 | Stimmauswahl-Pflicht, ffmpeg-Integration, Pfad-Konzept |
| 2.0.0 | 27.01.2026 | Korrektes MCP-Format, 28 EN Stimmen |
| 1.0.0 | 27.01.2026 | Initial Release |

---

*Version: 2.1.0*
*Abhängigkeiten: Kokoro (lokal), Chatterbox (HuggingFace MCP), ffmpeg*
