# Workflow Unification Project - Status

**Stand:** 27.01.2026
**Phase:** 3 (Testing & Erweiterung)

---

## ✅ ERLEDIGT

### Phase 1: Analyse & Konzeption (Chat)
- [x] Bestandsaufnahme vorhandener Skills (`/mnt/skills/user/`)
- [x] Feststellung: Methoden-Bibliothek fehlt (muss neu erstellt werden)
- [x] Self-Assessment Konzept entwickelt (DE + EN, mit Inhaltsfragen)
- [x] Vocabulary Sheet Konzept entwickelt (B2+ Format, Word Families)
- [x] Vokabel-Skill Konzept entwickelt (AWL-Prüfung, Extraktion aus Materialien)
- [x] Methoden-Index Variationssystem konzipiert (Tracking + Alternativen)
- [x] Timer-Folie Spezifikation (Arbeitsauftrag oben anzeigen)
- [x] Workflow-Reihenfolge geklärt (Vokabelliste NACH Materialien)
- [x] Hugging Face Bildgenerierung getestet (funktioniert)

### Phase 2: Implementierung (Cowork) ✅
- [x] **Methoden-Bibliothek Skill** erstellt
  - Speicherort: `/mnt/skills/user/methoden-bibliothek/SKILL.md`
  - Inhalt: 48 Methoden (15 Einstieg, 18 Erarbeitung, 15 Sicherung)
  - Register: Alphabetisch, nach Zeit, nach Sozialform

- [x] **Template-Dateien** erstellt
  - `/home/claude/templates/SELF_ASSESSMENT_DE.md`
  - `/home/claude/templates/SELF_ASSESSMENT_EN.md`
  - `/home/claude/templates/VOCABULARY_SHEET_TEMPLATE.md`

- [x] **Vokabel-Skill** erstellt
  - Speicherort: `/mnt/skills/user/vokabeln-zusammenfassen/SKILL.md`
  - Funktion: Extrahiert Vokabeln aus Materialien, AWL-Prüfung, Word Families

- [x] **Workflow-Skill** aktualisiert
  - Speicherort: `/mnt/skills/user/unterrichtsplanung-workflow/SKILL.md`
  - Ergänzungen: Handover-Struktur, Timer-Spezifikation, Methoden-Hinweis

- [x] **Hörverstehen-TTS Skill** erstellt ✅ NEU (27.01.2026)
  - Speicherort: `~/Library/Mobile Documents/com~apple~CloudDocs/Schule/Material/TTS/SKILL.md`
  - Version: 2.1.0
  - Features:
    - Kokoro TTS (lokal, 28 EN Stimmen)
    - Chatterbox (MCP, Voice Cloning)
    - ffmpeg-Integration (Audio zusammenführen, normalisieren)
    - Pflicht-Stimmauswahl vor jeder Generierung
    - Pfad-Konzept: Langzeit-Archiv + Arbeitskopie

### Konfiguration
- [x] Gemini MCP eingerichtet
- [x] Kokoro TTS lokal installiert (`~/kokoro-tts`)
- [x] ffmpeg verfügbar (`/opt/homebrew/bin/ffmpeg` v8.0.1)
- [x] ComfyUI lokal installiert (`~/ComfyUI`)

---

## 🔄 IN ARBEIT

### Phase 3: Testing & Validierung
- [x] Claude Desktop neustarten (damit neue Skills geladen werden)
- [x] Gemini MCP getestet
- [ ] Pilot-Test mit echtem Projekt (z.B. AV3_LWK)
- [ ] TTS-Skill in Cowork hochladen (`/mnt/skills/user/hoerverstehen-tts/`)

---

## ⏳ NOCH OFFEN

### Nach Pilot-Test
- [ ] PPTX-Vorlage mit Timer-Bibliothek erstellen (separate Aufgabe)
- [ ] Feedback aus Pilot einarbeiten
- [ ] Ggf. Skills anpassen

### Architektur-Fragen (später klären)
- [ ] Token-Effizienz: Methodenbibliothek erweitern oder schlank halten?
- [ ] Versionierung: Wie mit Template-Updates umgehen?
- [ ] Fallback: Was wenn Cowork nicht verfügbar?

---

## 📂 Aktuelle Dateistruktur

```
/mnt/skills/user/
├── arbeitsblatt-erstellen-v3/
│   ├── SKILL.md
│   └── templates/
├── methoden-bibliothek/
│   └── SKILL.md (17K, 48 Methoden)
├── unterrichts-medien/
│   └── SKILL.md (ComfyUI, Nanobanana, HuggingFace)
├── unterrichtsplanung-workflow/
│   └── SKILL.md (9K, Handover-System)
├── unterrichtsstunde-erstellen-v3/
│   ├── SKILL.md
│   └── templates/
└── vokabeln-zusammenfassen/
    └── SKILL.md (AWL, Word Families)

~/Library/Mobile Documents/com~apple~CloudDocs/Schule/Material/
├── TTS/
│   ├── SKILL.md (hoerverstehen-tts v2.1.0) ✅ NEU
│   ├── INSTALLATION.md
│   └── Audio/
│       ├── Listening/     ← Langzeit-Archiv
│       └── Voices/        ← Referenz-Stimmen für Chatterbox
└── ...

Google Drive (Meta-Projekt):
└── Claude-Meta-Projekt/skills/workflow/
    ├── workflow-unification-checklist.md ← DIESE DATEI
    ├── unterrichtsplanung-workflow-v4.zip
    └── unterrichtsplanung-workflow-v5.zip
```

---

## 📋 Workflow-Reihenfolge (Referenz)

### Englisch-Stunden (mit Hörverstehen):
1. Arbeitsblätter erstellen (arbeitsblatt-erstellen-v3)
2. Bilder/Grafiken generieren (unterrichts-medien)
3. **Audio für Hörverstehen erstellen** (hoerverstehen-tts) ← NEU
4. PowerPoint mit Timer-Folien (unterrichtsstunde-erstellen-v3)
5. **Vokabelliste erstellen** (vokabeln-zusammenfassen) ← aus Materialien
6. Self-Assessment erstellen

### Andere Fächer:
1. Arbeitsblätter erstellen
2. Bilder/Grafiken generieren
3. PowerPoint mit Timer-Folien
4. Self-Assessment erstellen

---

## 🎤 TTS Quick Reference

**Kokoro (Standard):**
```javascript
Control your Mac:osascript({
  script: 'source ~/kokoro-tts/bin/activate && python3 ...'
})
```

**Empfohlene Stimmen:**
| Typ | Stimme | Verwendung |
|-----|--------|------------|
| US Female | `af_heart` | Dialog (Standard) |
| US Female | `af_sarah` | Diktat (klar) |
| US Male | `am_michael` | Nachrichten |
| UK Female | `bf_emma` | UK Standard |
| UK Male | `bm_george` | UK Standard |

**Pfad-Konzept:**
- Langzeit: `~/...iCloud.../Schule/Material/TTS/Audio/Listening/`
- Arbeitskopie: `~/...iCloud.../Schule/Unterricht/[KLASSE]/[EINHEIT]/Audio/`

---

## 🔗 Referenzen

- Übergabeprotokoll: Chat vom 17.01.2025
- Methoden-Bibliothek: `/mnt/skills/user/methoden-bibliothek/SKILL.md`
- Templates: `/home/claude/templates/`
- Vokabel-Skill: `/mnt/skills/user/vokabeln-zusammenfassen/SKILL.md`
- **TTS-Skill: `~/...iCloud.../Schule/Material/TTS/SKILL.md`** ← NEU

---

## 📝 Notizen & Entscheidungen

### 17.01.2025
- [ENTSCHEIDUNG] Vokabelliste wird NACH Materialien erstellt (nicht davor)
- [ENTSCHEIDUNG] Self-Assessment hat 4-6 Inhaltsfragen (Teil A) + Reflexion (Teil B-D)
- [ENTSCHEIDUNG] Vocabulary Sheet nur B2+, keine deutsche Übersetzung
- [ENTSCHEIDUNG] Timer-Folie zeigt Arbeitsauftrag OBEN an
- [ENTSCHEIDUNG] Methoden-Tracking: Variation nach 3 Stunden erzwingen

### 27.01.2026
- [ENTSCHEIDUNG] TTS-Skill nutzt Kokoro (lokal) als Standard, Chatterbox (MCP) für Voice Cloning
- [ENTSCHEIDUNG] Pflicht-Stimmauswahl: Bei JEDER Audio-Generierung Auswahl anzeigen
- [ENTSCHEIDUNG] Pfad-Konzept: Langzeit-Archiv (iCloud TTS/) + Arbeitskopie (Unterricht/)
- [ENTSCHEIDUNG] 28 englische Stimmen verfügbar (nicht 31 wie ursprünglich dokumentiert)
- [ENTSCHEIDUNG] ffmpeg für Audio-Concat, Normalisierung, MP3-Konvertierung nutzen
- [ENTSCHEIDUNG] MCP-Format: `Hugging Face:dynamic_space` (nicht UUID-basiert)
- [ENTSCHEIDUNG] INSTALLATION.md als Backup behalten (falls Neuinstallation nötig)
