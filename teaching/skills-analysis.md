# Analyse: Toms Skills & Workflows
**Stand:** 03.02.2026  
**Analysiert von:** Subagent (OpenClaw)  
**Quelle:** `/tmp/skills_extracted/skills/` (aus Claude Desktop)

---

## 📋 Übersicht

Tom hat ein hochentwickeltes **Unterrichtsplanungs-Ecosystem** für Claude Desktop entwickelt. Die Skills decken den gesamten Workflow ab: Von der Konzeption über Materialerstellung bis zu interaktiven Lernformaten.

**Kernelemente:**
- **Strukturierter 2-Phasen-Workflow** (Planung → Materialerstellung)
- **Template-System** für konsistente Dokumente
- **Methoden-Bibliothek** mit 48+ Unterrichtsmethoden
- **TTS-Integration** für Hörverstehensaufgaben
- **H5P-Generator** für interaktive Lernmaterialien
- **PowerPoint-Automation** mit Timer-Integration
- **Bildgenerierung** via ComfyUI

---

## 🔥 Top-Priority Skills (Sofort integrierbar)

### 1. **Workflow-Skill** (`workflow/`)
**Zweck:** Meta-Orchestrierung der gesamten Unterrichtsplanung  
**Version:** v5.1 (neueste: v5+)  
**Status:** ⭐ **KERNSTÜCK DES SYSTEMS**

#### Was macht es?
- **2-Phasen-System:** Chat (Planung) ↔ Cowork (Ausführung)
- **6 Kernprinzipien:**
  1. Roter Faden (Story-Check nach jeder Stunde)
  2. Hybrid Chat↔Cowork Aufteilung
  3. Textformat-Abfrage (Zeitungsartikel, Scientific Paper, etc.)
  4. Sequentielle Stundenplanung (nie mehrere Stunden parallel!)
  5. ComfyUI-Automation
  6. **SKILL-PFLICHT-CHECK** (verhindert "von Grund auf neu bauen")
- **Handover-System:** Übergabeprotokoll mit FERTIG GESCHRIEBENEN Texten
- **Methoden-Tracking:** Variationsformel (max. 3x gleiche Methode)

#### Technische Details
- **Templates:** HANDOVER_TEMPLATE.md, COWORK_PROMPT.md, STUNDEN_CHECKLISTE.md
- **Self-Assessment:** DE + EN Versionen
- **Methoden-Historie:** Tracking über Stunden hinweg
- **Trigger:** "Unterricht planen", "Handover", "für Cowork"

#### Dependencies
- `methoden-bibliothek` (Methodenwahl + Variation)
- `arbeitsblatt-erstellen-v3` (Word-Dokumente)
- `unterrichtsstunde-erstellen-v3` (PowerPoint)
- `unterrichts-medien` (Bildgenerierung)
- `vokabeln-zusammenfassen` (nur Englisch)

#### OpenClaw-Anpassungen nötig:
- ✅ **Direkt nutzbar** als Workflow-Anleitung
- ⚠️ Pfade anpassen (Claude Desktop nutzt `/mnt/skills/user/`, wir nutzen `teaching/skills/`)
- ⚠️ "Control your Mac:osascript" → OpenClaw `exec` ersetzen
- ⚠️ "Cowork" Konzept → OpenClaw Subagents oder strukturierte Workflows

---

### 2. **Methoden-Bibliothek** (`methoden-bibliothek/`)
**Zweck:** Umfassende Sammlung von Unterrichtsmethoden  
**Status:** ⭐ **KERNRESSOURCE**

#### Inhalt
**651 Zeilen, 48+ Methoden** in drei Kategorien:
- **Einstieg/Aktivierung (15):** Bildimpuls, Zitat-Reaktion, Mini-Mystery, Think-Pair-Share, Concept Cartoon, etc.
- **Erarbeitung (18):** Gruppenpuzzle, Advance Organizer, Texterschließung, Rollenkarten, etc.
- **Sicherung (15):** Exit Ticket, Concept Map, Lerntagebuch, Blitzlicht Strukturiert, etc.

#### Struktur pro Methode
```markdown
### Methodenname
**Dauer:** 5-10 Min | **Sozialform:** EA/PA/GA/Plenum
**Material:** Was wird benötigt
**Ablauf:**
1. Schritt 1
2. Schritt 2
...
**Varianten:** Alternative Durchführungen
**Geeignet für:** Kontexte
```

#### OpenClaw-Integration:
- ✅ **Direkt nutzbar** als Markdown-Datenbank
- 💡 **Idee:** In Notion Methods-DB integrieren (zusätzliche Quellen)
- 💡 **Idee:** Vektordatenbank für semantische Suche (z.B. "Methode für schüchterne Klasse")

---

### 3. **TTS-Skill** (`TTS/`)
**Zweck:** Audio-Generierung für Hörverstehensaufgaben  
**Version:** v2.2 (neueste Version)  
**Status:** 🎤 **PRODUCTION READY**

#### Features
- **Kokoro TTS (lokal):**
  - 28 englische Stimmen (US + UK)
  - Kostenlos, offline, schnell
  - Automatisches Chunking (bis ~10 Min Audio)
  - Sample: `af_heart` (US warm), `bf_emma` (UK elegant)
- **Chatterbox (MCP):**
  - Voice Cloning (5-10 Sek. Referenz-Audio)
  - Emotionale Tags: `[laughs]`, `[sighs]`
  - Limit: 300 Zeichen pro Request
- **ffmpeg-Integration:**
  - Audio zusammenführen
  - Lautstärke normalisieren
  - WAV → MP3 Konvertierung

#### Workflow
1. **Stimmauswahl** (PFLICHT bei jeder Generierung!)
2. **Audio generieren** → Langzeit-Archiv (`~/...iCloud.../Schule/Material/TTS/Audio/Listening/`)
3. **Arbeitskopie** → Projektordner (`~/...iCloud.../Schule/Unterricht/[KLASSE]/[EINHEIT]/Audio/`)

#### Dateinamen-Konvention
```
[Klasse]_[Einheit]_Track[Nr]_[Beschreibung].wav
Beispiel: 10a_Unit5_Track01_Introduction.wav
```

#### OpenClaw-Anpassungen:
- ⚠️ **Kokoro TTS:** Lokal installiert bei Tom (`~/kokoro-tts`), würde bei uns nicht funktionieren (keine lokale macOS-Umgebung)
- ✅ **Alternative:** OpenClaw hat bereits `tts` Tool (ElevenLabs via `/usr/local/bin/sag`)
- 💡 **Idee:** Stimmenauswahl-UI für ElevenLabs entwickeln (ähnlich zu Toms Kokoro-Auswahl)
- 💡 **Idee:** ffmpeg-Funktionen (concat, normalize) als Helper-Script
- ⚠️ **Chatterbox MCP:** Nutzt Hugging Face Space, bei uns als `web_fetch` + API nutzbar

#### Praxisrelevanz für Mammutprojekt:
🎯 **SEHR RELEVANT!** Mammutprojekt braucht Audio-Storytelling. Das TTS-Konzept (Stimmauswahl, Multi-Speaker-Dialoge, Datei-Organisation) ist 1:1 übertragbar.

---

### 4. **H5P-Generator** (`h5p-generator/`)
**Zweck:** Interaktive Lernmaterialien programmatisch erstellen  
**Status:** 🐍 **PYTHON-TOOL**

#### Unterstützte Content-Typen
1. **Multiple Choice** — Single/Multi-Answer
2. **Fill in the Blanks** — Lückentexte (`*Antwort*` Syntax)
3. **True/False** — Wahr/Falsch-Fragen
4. **Flashcards** — Vokabelkarten (Front/Back)
5. **Quiz (Question Set)** — Kombiniert alle obigen Typen

#### Python API
```python
from h5p_generator import H5PGenerator, MultipleChoice

mc = MultipleChoice(
    question="Was ist die Hauptstadt von Frankreich?",
    answers=["London", "Paris", "Berlin"],
    correct=1
)

generator = H5PGenerator(output_dir="./output")
generator.create_multichoice("france_quiz", mc)
# → Erstellt france_quiz.h5p
```

#### JSON-Format (auch via CLI)
```bash
python h5p_generator.py quiz input.json -o ./output
```

#### Output
`.h5p` Dateien (ZIP-Archive) importierbar in:
- Moodle (mit H5P Plugin)
- WordPress (mit H5P Plugin)
- H5P.com
- Lumi Desktop App

#### OpenClaw-Integration:
- ✅ **Direkt nutzbar** (Python, keine Dependencies außer stdlib)
- 💡 **Idee:** Als `teaching/tools/h5p_generator.py` integrieren
- 💡 **Idee:** Wrapper-Skill erstellen: "Erstelle H5P Quiz aus diesem Text"
- 🎯 **Relevanz:** Hoch für interaktive Lernmaterialien, besonders für AV/Berufskollege-Szenarien

---

## 📦 Weitere Skills (Wichtig, aber mit Anpassungsbedarf)

### 5. **Arbeitsblatt-Erstellen** (`doc/`)
**Zweck:** Word-Dokumente (.docx) für Unterricht  
**Version:** v3 (neueste)  
**Template-basiert:** `Vorlage_Fach.docx`, `Vorlage_Klassenarbeit.docx`

#### Features
- **Design-System:** Einheitliche Headers, Footer, Schriftarten
- **Platzhalter-Ersetzung:** `[Thema]`, `[Datum]`, `[Arbeitsauftrag]`, etc.
- **PFLICHT-Nutzung:** Für ALLE .docx im Unterricht (verhindert "von Grund auf neu bauen")
- **Encoding-Regel:** IMMER echte Umlaute (ä, ö, ü), niemals ae/oe/ue
- **Validierung:** Nach Erstellung auf Platzhalter + Umlaute prüfen

#### Trigger (v3 erweitert)
- Explizit: "Arbeitsblatt erstellen", "AB erstellen", "Infoblatt"
- Implizit: Country Profiles, Crisis Briefings, Structured Notes, Position Matrix, Phrase Sheets

#### OpenClaw-Anpassungen:
- ⚠️ **python-docx Dependency** (bei Tom via `/mnt/skills/user/`)
- ⚠️ **Templates:** Müssen in OpenClaw Workspace kopiert werden
- 💡 **Alternative:** LibreOffice Headless + Templates (via `exec`)
- 💡 **Alternative:** Markdown → DOCX Konvertierung (pandoc)

---

### 6. **PowerPoint-Erstellen** (`pptx/`)
**Zweck:** Unterrichtspräsentationen mit Timer-Integration  
**Version:** v4  
**Hybrid-System:** pptxgenjs (von Scratch) + python-pptx (Template + Video)

#### Features
- **Timer-Videos:** 4, 5, 10 Min im Skill; 3-30 Min extern verfügbar
- **python-pptx:** Für Templates + Video-Einbettung
- **pptxgenjs:** Für Von-Scratch-Erstellung (ohne Video)
- **Design-System:** Layout-Vorlagen für verschiedene Folientypen

#### Timer-Integration
```python
from pptx import Presentation
prs = Presentation("Vorlage.pptx")
slide = prs.slides.add_slide(prs.slide_layouts[5])

timer_path = "/path/to/timer_pixel_5min.mp4"
slide.shapes.add_movie(timer_path, left, top, width, height)
```

#### OpenClaw-Anpassungen:
- ⚠️ **python-pptx + pptxgenjs:** Python + Node.js Dependencies
- ⚠️ **Timer-Videos:** Externe Abhängigkeit (Tom hat Sammlung in Google Drive)
- 💡 **Alternative:** Timer als SVG/Canvas generieren (CSS Animation)
- 💡 **Alternative:** reveal.js Präsentationen (Web-basiert, Timer via JS)

---

### 7. **Unterrichts-Medien** (`unterricht-medien/`)
**Zweck:** Bildgenerierung für Unterrichtsmaterialien  
**Version:** v3.1  
**Primär:** ComfyUI (lokal) mit Fallback-Kaskade

#### Tools
1. **ComfyUI (lokal):** FLUX.1-schnell, kostenlos, offline
2. **Fallback 1:** nanobanana (Gemini-basiert, MCP)
3. **Fallback 2:** Hugging Face Turbo

#### FLUX-Prompt-Struktur
```
Subject → Action → Style → Technical
❌ KEINE Quality Tags ("masterpiece", "8k")
❌ KEINE Künstlernamen
```

#### OpenClaw-Anpassungen:
- ⚠️ **ComfyUI:** Läuft lokal bei Tom, nicht in OpenClaw Gateway
- ✅ **Alternative:** OpenClaw könnte Node mit ComfyUI nutzen (wenn verfügbar)
- ✅ **Alternative:** Hugging Face Image Generation via `web_fetch` + API
- 💡 **Idee:** Midjourney/DALL-E Integration (wir haben keine ComfyUI-Instanz)

---

## 🔄 Skills-Interaktion & Dependencies

```
┌─────────────────────────────────────────────────────────────────┐
│                   WORKFLOW-SKILL (Orchestrator)                 │
│                                                                 │
│  Phase 1 (Chat):  Planung + Story-Check + Methodenwahl         │
│  Phase 1.5:       Handover-Erstellung                          │
│  Phase 2 (Cowork): Materialerstellung                          │
└─────────────────────────────────────────────────────────────────┘
           │
           ├─── Methodenwahl ───────► METHODEN-BIBLIOTHEK
           │                          (48 Methoden, Variation)
           │
           ├─── Materialerstellung ──┬─► ARBEITSBLATT-ERSTELLEN
           │                         │   (Word, Templates)
           │                         │
           │                         ├─► POWERPOINT-ERSTELLEN
           │                         │   (python-pptx, Timer)
           │                         │
           │                         ├─► UNTERRICHTS-MEDIEN
           │                         │   (ComfyUI/Fallback)
           │                         │
           │                         └─► TTS (nur Englisch)
           │                             (Kokoro/Chatterbox)
           │
           └─── Optional ────────────┬─► H5P-GENERATOR
                                     │   (Interaktive Materialien)
                                     │
                                     └─► VOKABELN-ZUSAMMENFASSEN
                                         (nur Englisch, AWL)
```

---

## 🎯 OpenClaw-Integrationsstrategie

### Phase 1: Foundation (Sofort)
1. **Methoden-Bibliothek** → `/teaching/methods.md` (direkt kopieren)
2. **Workflow-Konzept** → `/teaching/workflow.md` (angepasst ohne Claude Desktop Spezifika)
3. **H5P-Generator** → `/teaching/tools/h5p_generator.py` (1:1 kopieren)

### Phase 2: Adaptationen (Kurzfristig)
4. **TTS-Konzept** adaptieren:
   - Stimmauswahl-UI für ElevenLabs
   - Multi-Speaker-Dialog Workflow
   - ffmpeg Helper-Scripts
5. **Templates erstellen:**
   - Markdown → DOCX Pipeline (pandoc)
   - Reveal.js Präsentations-Templates (statt PPTX)
6. **Bildgenerierung:**
   - Hugging Face API Integration
   - Prompt-Templates für FLUX/DALL-E

### Phase 3: Automation (Mittelfristig)
7. **Workflow-Orchestrierung:**
   - Handover-System mit OpenClaw Subagents
   - Automatische Skill-Auswahl
   - Validierungs-Checks
8. **Methoden-Tracking:**
   - Variationsformel implementieren
   - Historie in Notion/Local DB

---

## 💡 Was können wir DIREKT übernehmen?

### ✅ Ohne Änderungen nutzbar:
1. **Methoden-Bibliothek** (651 Zeilen Markdown) → Teaching Methods DB
2. **H5P-Generator** (Python, stdlib-only) → Interaktive Materialien
3. **Workflow-Prinzipien** (6 Kernprinzipien, Story-Check, Sequentielle Planung)
4. **Template-Konzepte** (Handover-Struktur, Checklisten, Self-Assessment)
5. **TTS-Workflow** (Stimmauswahl, Dateinamen, Archiv-Struktur)

### ⚠️ Mit Anpassungen nutzbar:
6. **Arbeitsblatt-Erstellen** (Templates + python-docx OR pandoc)
7. **PowerPoint-Erstellen** (reveal.js statt PPTX OR python-pptx via Node)
8. **Bildgenerierung** (Hugging Face API statt ComfyUI)
9. **TTS-Generierung** (ElevenLabs statt Kokoro)

### ❌ Nicht direkt übertragbar (aber inspirierend):
10. **Cowork-Spezifika** (Claude Desktop MCP Server, `/mnt/skills/user/` Pfade)
11. **ComfyUI-Integration** (Tom hat lokale Instanz, wir nicht)
12. **osascript-Commands** (macOS-spezifisch, Tom steuert Host-System)

---

## 🚀 Quick-Win-Implementierung (48h)

### Schritt 1: Methoden-Bibliothek kopieren
```bash
cp teaching/tom-skills/methoden-bibliothek/methoden-bibliothek.md \
   teaching/methods-library.md
```

### Schritt 2: H5P-Generator integrieren
```bash
cp teaching/tom-skills/h5p-generator/h5p_generator.py \
   teaching/tools/
chmod +x teaching/tools/h5p_generator.py
```

### Schritt 3: Workflow-Skill anpassen
```bash
# Erstelle teaching/workflow.md mit:
# - 6 Kernprinzipien
# - Handover-Template (angepasst für OpenClaw)
# - Story-Check Konzept
# - Methoden-Variationsformel
```

### Schritt 4: TTS-Konzept dokumentieren
```bash
# Erstelle teaching/tts-workflow.md mit:
# - ElevenLabs Stimmen-Mapping (analog zu Kokoro)
# - Multi-Speaker-Dialog Pattern
# - Audio-Archiv-Struktur
```

---

## 📝 Was fehlt noch?

### Templates
- [ ] Word-Templates (Vorlage_Fach.docx) → In OpenClaw Format konvertieren
- [ ] PowerPoint-Timer-Videos → Alternativen finden oder selbst erstellen
- [ ] Self-Assessment Templates (DE + EN) → Vorhanden in Workflow!

### Tools
- [ ] ffmpeg Helper-Scripts (Audio concat, normalize) → Einfach zu erstellen
- [ ] Pandoc Wrapper (Markdown → DOCX) → Standard-Tool, verfügbar
- [ ] Image API Abstraction (Hugging Face + Fallbacks) → Mittlerer Aufwand

### Datenbanken
- [ ] Methoden-Tracking DB (SQLite oder Notion) → Für Variationsformel
- [ ] Material-Archiv (Notion oder Local) → Für Wiederverwendung

---

## 🎓 Toms Pädagogischer Kontext

**Schulformen:**
- AV (Ausbildungsvorbereitung)
- Berufskolleg Sozialpädagogik
- Berufliches Gymnasium

**Fächer:**
- Englisch
- Politik/Geschichte
- Lebensweltkunde

**Typische Unterrichtsformate:**
- Simulationen (z.B. NATO Crisis Simulation)
- Projekt-basiertes Lernen
- Hörverstehensaufgaben (Englisch)
- Interaktive Materialien (H5P)
- Multi-Session Units (3-5 Stunden)

**Besonderheiten:**
- Bilinguale Module (Englisch + Fachinhalt)
- B2+ Sprachniveau
- Academic Word List (AWL) Integration
- Self-Assessment nach jeder Einheit

---

## 🔗 Verknüpfung mit bestehendem System

### Methods-DB (Notion)
- Toms Methoden-Bibliothek als zusätzliche Quelle
- 48 neue Methoden mit Durchführungsdetails
- Ergänzt bestehende Sammlung

### Mammutprojekt
- TTS-Workflow für Audio-Storytelling
- Multi-Speaker-Dialoge (Charaktere)
- Archiv-Struktur für Audio-Files

### Teaching-Games
- H5P-Generator für interaktive Quizze
- Flashcard-System für Vokabeln
- True/False Mechanics

---

## 🎯 Empfehlungen

### Priorität 1 (Diese Woche):
1. ✅ Methoden-Bibliothek kopieren → `teaching/methods-library.md`
2. ✅ H5P-Generator installieren → `teaching/tools/h5p_generator.py`
3. ✅ Workflow-Prinzipien dokumentieren → `teaching/workflow-principles.md`

### Priorität 2 (Nächste Woche):
4. TTS-Workflow adaptieren (ElevenLabs Mapping)
5. Handover-Template für OpenClaw erstellen
6. Bildgenerierungs-Helper (Hugging Face API)

### Priorität 3 (Nächster Monat):
7. Template-System (Markdown → DOCX Pipeline)
8. Methoden-Tracking DB (Variationsformel)
9. Reveal.js Präsentations-System (statt PPTX)

---

## 📊 Statistik

| Skill | Dateien | Lines of Code | Status |
|-------|---------|---------------|--------|
| **workflow** | 7 | ~2.500 | 🟢 Vollständig |
| **methoden-bibliothek** | 1 | 651 | 🟢 Vollständig |
| **TTS** | 3 | ~800 | 🟢 Vollständig |
| **h5p-generator** | 4 | ~850 | 🟢 Vollständig |
| **arbeitsblatt-erstellen** | 3 | ~500 | 🟢 Vollständig |
| **pptx** | 10+ | ~2.000+ | 🟢 Vollständig |
| **unterricht-medien** | 3 | ~700 | 🟢 Vollständig |

**Gesamt:** ~30 Dateien, ~7.000 Lines of Code/Dokumentation

---

## 🏁 Fazit

Tom hat ein **professionelles, produktionsreifes Teaching-System** entwickelt. Die Skills sind:
- ✅ Gut dokumentiert
- ✅ Versioniert (v2, v3, v4, v5)
- ✅ Mit Error Prevention ausgestattet
- ✅ Template-basiert (konsistent)
- ✅ Modular & erweiterbar

**Größte Stärke:** Der **Workflow-Skill** als Orchestrator mit klaren Prinzipien (Story-Check, Sequentielle Planung, Skill-Pflicht-Check) verhindert chaotische Ad-hoc-Materialerstellung.

**Größte Herausforderung für OpenClaw:** Anpassung der lokalen Tool-Abhängigkeiten (ComfyUI, Kokoro TTS, python-docx, python-pptx) an OpenClaw-Umgebung (Gateway, keine macOS Host-Kontrolle).

**Empfehlung:** Kernkonzepte übernehmen (Workflow, Methoden, H5P), Tools adaptieren (ElevenLabs statt Kokoro, Hugging Face statt ComfyUI, Pandoc statt python-docx).

---

*Analysiert am: 03.02.2026*  
*Nächste Schritte: Siehe "Quick-Win-Implementierung (48h)"*
