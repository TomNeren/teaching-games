---
name: unterrichtsplanung-workflow
description: Strukturierter 2-Phasen-Workflow für Unterrichtsplanung. PHASE 1 (Chat) bei "Unterricht planen", "Stunde planen", "neue Stunde", "planen", "hilf mir". PHASE 1.5 (create HANDOVER for cowork) bei "Übergabeprotokoll", "Handover", "für Cowork", "Materialerstellung" - nutzt HANDOVER_TEMPLATE. Enthält 6 Kernprinzipien und COWORK_PROMPT für Materialerstellung.
---

# Unterrichtsplanung Workflow Skill (v5.0)

**Version:** 5.1.0
**Stand:** 29.01.2026
**Changelog:** PHASE 2 TRIGGER hinzugefügt (Übergabeprotokoll, Handover, für Cowork), Erkennungsmerkmale für Handover, automatisches Skill-Loading bei Phase 2

Dieser Skill definiert einen zweiphasigen Workflow für die Unterrichtsplanung mit klarer Trennung zwischen kreativer Ideenfindung (Chat) und technischer Materialerstellung (Cowork).

---

## Skill-Inhalt (Ordnerstruktur)

```
/mnt/skills/user/unterrichtsplanung-workflow/
├── SKILL.md                              # Diese Datei
└── templates/
    ├── HANDOVER_TEMPLATE.md              # Übergabeprotokoll Chat→Cowork
    ├── COWORK_PROMPT.md                  # Ausführungsanweisung für Cowork
    ├── STUNDEN_CHECKLISTE.md             # Validierung nach jeder Stunde
    ├── METHODEN_HISTORIE_TEMPLATE.md     # Tracking vergangener Methoden
    ├── SELF_ASSESSMENT_DE.md             # Self-Assessment (Deutsch)
    └── SELF_ASSESSMENT_EN.md             # Self-Assessment (Englisch)
```

---

## 🚨 WHEN TO USE THIS SKILL (TRIGGER)

### PHASE 1 Trigger (Chat - Planung)

**Aktiviere diesen Skill bei:**
- "Unterricht planen", "Stunde planen", "Einheit planen"
- "Unterrichtsplanung", "Stundenplanung"
- "neue Stunde", "neue Einheit", "neues Projekt"
- Jede Anfrage zu Unterrichtsmaterialien für Schule

**Aktion:** Workflow Phase 1 starten (kreative Planung)

---

### PHASE 1,5 Trigger (Übergabeprotokoll) ⚠️ KRITISCH!


```
┌─────────────────────────────────────────────────────────────────┐
│  🚨 PHASE 1.5 TRIGGER                                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  • "Übergabeprotokoll"                                          │
│  • "Handover"                                                   │
│  • "für Cowork"                                                 │
│  • "Materialerstellung"                                         │
│  • "Materialien erstellen"                                      │
│  • "jetzt erstellen"                                            │
│  • "PFLICHT-SKILLS"                                             │
│  • Dokument mit "Projekt-ID" und "Metadaten" Tabelle            │
│                                                                 │
│  → HANDOVER_TEMPLATE                                            │
│                                                                 │
│  → COWORK_PROMPT.md als Ausführungsanweisung verwenden!         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```


---

## ⚡ 6 KERNPRINZIPIEN (NEU: #6 in v5.0)

### 1. 🧵 ROTER FADEN (Story-Telling)

**Problem:** Phasen nicht aufeinander abgestimmt, kein Sinn warum Phase X auf Y folgt

**Lösung:**
- Claude denkt den roten Faden PROAKTIV während der Planung mit
- AM ENDE jeder Stunde: PFLICHT-Story-Check

```
🧵 STORY-CHECK Stunde {{NR}}:

1. EINSTIEG → Verbindung zu Erarbeitung 1: [Erklärung]
2. ERARBEITUNG 1 → Verbindung zu Erarbeitung 2: [Erklärung]
3. ERARBEITUNG 2 → Verbindung zu Sicherung: [Erklärung]
4. SICHERUNG → Verbindung zu Abschluss: [Erklärung]

❓ Ist diese Story konsistent? [User muss bestätigen]
```

**Regel:** User muss Story-Check bestätigen bevor Stunde als "fertig" gilt!

---

### 2. 🔀 HYBRID CHAT↔COWORK AUFTEILUNG

**Analyse:** Cowork verbraucht mehr Tokens, Chat hat mehr Kapazität für Kreativität

| Chat (Kreativ) | Cowork (Technisch) |
|----------------|-------------------|
| Konzept entwickeln | **Skills laden (PFLICHT!)** |
| Roter Faden durchdenken | **Vorlagen laden (PFLICHT!)** |
| Methodenwahl (mit Variation) | Platzhalter ersetzen |
| **FERTIGE Arbeitsaufträge** schreiben | Bilder generieren (ComfyUI) |
| **FERTIGE AB-Texte** schreiben | Timer einfügen |
| Bild-Prompts formulieren | PPT erstellen |
| Story-Check durchführen | Dateien organisieren |
| | Validierung ausführen |

**Konsequenz:** Das Handover enthält FERTIGE TEXTE, nicht nur Stichpunkte!

---

### 3. 📄 TEXTFORMAT-ABFRAGE

**Problem:** Texte als Argumentation geliefert statt gewünschtem Format (Zeitungsartikel, Scientific Paper)

**Lösung:** Bei JEDER Textgenerierung für Materialien explizit fragen:

```
📄 TEXTFORMAT-ABFRAGE

Welches Format soll der Text haben?
□ Zeitungsartikel (Überschrift, Lead, Fließtext)
□ Wissenschaftlicher Text (Abstract, Einleitung, Hauptteil, Fazit)
□ Argumentation (These → Argumente → Fazit)
□ Sachtext (neutral, informativ)
□ Dialog (Gesprächsformat)
□ Erzählung (narrativ)
□ Anleitung (Schritt-für-Schritt)
□ Anderes: ____________

→ Nach Auswahl: Format STRIKT einhalten!
```

---

### 4. 📊 SEQUENTIELLE STUNDENPLANUNG

**Problem:** Stunde 1 sorgfältig, Stunden 2-5 nur umrissen, User sagt "ja ja, passt schon"

**Lösung:**
- EINE Stunde komplett durcharbeiten (Konzept → Roter Faden → Texte → Story-Check)
- Dann erst nächste Stunde
- Claude akzeptiert NICHT bei "passt schon":

```
⚠️ WORKFLOW-ERINNERUNG

Bevor wir zur nächsten Stunde gehen:
□ Roter Faden geprüft?
□ Story-Check bestätigt?
□ ALLE Arbeitsaufträge ausformuliert?
□ Alle Texte geschrieben?

🎯 LIEBER: 2 durchdachte Stunden ALS 5 skizzierte
```

---

### 5. 🖼️ COMFYUI-AUTOMATION

**Workflow in Cowork (automatisch):**

```bash
# 1. ComfyUI starten
open -a "ComfyUI"

# 2. Warten bis Server bereit
until curl -s http://127.0.0.1:8188 > /dev/null; do
    sleep 2
done

# 3. Bilder generieren (MCP Tool)
mcp__comfyui__generate_image für jedes Bild

# 4. ComfyUI schließen
osascript -e 'quit app "ComfyUI"'
```

**Fallback-Kaskade:**
1. ComfyUI (lokal) → Beste Qualität
2. mcp__nanobanana__generate_image → Gemini-basiert
3. mcp__fa86031e-8beb-4aac-b517-e3b796ddf8ec__gr4_z_image_turbo_generate → Schnell

---

### 6. 🚨 SKILL-PFLICHT-CHECK (NEU in v5.0!)

**Problem aus v4:** Skills wurden trotz Verfügbarkeit nicht verwendet! Eigene Scripts von Grund auf erstellt statt Vorlagen zu laden.

**Ursachen (analysiert):**
1. Trigger-Keywords zu eng definiert (40%)
2. Skill-Beschreibungen zu spezifisch (25%)
3. "Effizienz" priorisiert über Konsistenz (25%)
4. Keine explizite Skill-Referenz im Handover (10%)

**LÖSUNG: PFLICHT-CHECK VOR JEDER DATEI-ERSTELLUNG!**

```
┌─────────────────────────────────────────────────────────────────────────┐
│  🚨 SKILL-PFLICHT-CHECK VOR MATERIALERSTELLUNG                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  FRAGE: Welche Datei soll erstellt werden?                              │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │ .docx für Unterricht?                                           │    │
│  │ → arbeitsblatt-erstellen-v3 PFLICHT!                            │    │
│  │ → Auch für: Infoblätter, Country Profiles, Crisis Briefings,    │    │
│  │             Structured Notes, Position Matrix, Phrase Sheets    │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │ .pptx für Unterricht?                                           │    │
│  │ → unterrichtsstunde-erstellen-v3 PFLICHT!                       │    │
│  │ → Auch für: Simulationen, Multi-Session PPTs, Workshop Slides   │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │ Bilder für Unterricht?                                          │    │
│  │ → unterrichts-medien PFLICHT!                                   │    │
│  │ → ComfyUI  → Hugging Face                           │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                                                         │
│  ⚠️ NIEMALS eigene Scripts von Grund auf erstellen wenn Skill          │
│     mit Vorlage verfügbar ist!                                          │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

**Konsequenz für Handover:**
- Das Übergabeprotokoll MUSS die zu verwendenden Skills explizit listen
- Cowork-Prompt MUSS mit Skill-Lesen beginnen

---

## 🔀 METHODEN-TRACKING (Persistente Variation)

### Das Problem

Die Variationsformel (max. 3x gleiche Methode) kann nicht greifen ohne historische Daten.

### Die Lösung: Zwei-Komponenten-System

| Komponente | Zweck | Speicherort |
|------------|-------|-------------|
| **methoden-historie.md** | Tracking vergangener Methoden | Project Knowledge |
| **methoden-bibliothek** | Alternativen finden | `/mnt/skills/user/methoden-bibliothek/SKILL.md` |

---

### Variationsformel

| Verwendungen in Folge | Status | Aktion |
|----------------------|--------|--------|
| 1x | ✅ OK | Frei verwendbar |
| 2x | ⚠️ Warnung | Alternative aus methoden-bibliothek vorschlagen |
| 3x | 🔴 Gesperrt | NICHT mehr verwenden, Alternative PFLICHT |

---

## ⚡ KRITISCHE REGELN

### 1. ENCODING (Umlaute) - IMMER!
```
✅ RICHTIG: ä, ö, ü, ß, Ä, Ö, Ü
❌ FALSCH:  ae, oe, ue, ss, Ae, Oe, Ue

NIEMALS ae/oe/ue verwenden! Immer echte Umlaute!
```

### 2. PLATZHALTER vollständig ersetzen
```
Nach Erstellung darf KEIN [...] mehr im Dokument sein!
→ Validierung nach JEDEM Dokument ausführen
```

### 3. PROTOKOLL ist verbindlich
```
Das Übergabeprotokoll definiert EXAKT was erstellt wird.
→ Folienanzahl, Timer-Zeiten, Bilder - alles aus Protokoll!
```

### 4. SKILLS VOR EIGENEN SCRIPTS (NEU!)
```
IMMER zuerst prüfen ob ein Skill mit Vorlage existiert!
→ Vorlage laden > Eigenes Script schreiben
```

---

## Core Workflow

### Phase 1: Ideenfindung & Stundenentwicklung (Chat)

**Ziel**: Kreative, flexible Entwicklung der Unterrichtsstunde

**Vorgehen (SEQUENTIELL - eine Stunde nach der anderen!):**

1. **VOR BEGINN:** methoden-historie.md lesen (wenn vorhanden)

2. **PRO STUNDE:**
   - Konzept entwickeln
   - Roter Faden durchdenken (Claude proaktiv!)
   - Methoden wählen (Variationsformel beachten!)
   - Bei Texten: Textformat abfragen
   - Texte VOLLSTÄNDIG ausarbeiten (Arbeitsaufträge, AB-Inhalte)
   - Bild-Prompts formulieren
   - **STORY-CHECK (PFLICHT!)** - User muss bestätigen

3. **DANN ERST:** Nächste Stunde ODER Handover

**Indikatoren für Ende von Phase 1:**
- Alle Stunden haben Story-Check bestanden
- Alle Texte sind vollständig ausformuliert
- Alle Bild-Prompts definiert
- Der Lehrer signalisiert Bereitschaft zur Materialerstellung

---

### Phase 1.5: Übergabe vorbereiten (Chat)

**Am Ende von Phase 1 erstellt Chat DREI Dokumente:**

1. **Übergabeprotokoll** (HANDOVER_TEMPLATE.md)
   - Vollständige Spezifikation aller Materialien
   - FERTIGE Texte (nicht nur Stichpunkte!)
   - PPT-Struktur Folie für Folie
   - Bild-Prompts
   - **NEU: Explizite SKILL-REFERENZEN!**

2. **methoden-historie-update.md** (für Project Knowledge)
   - Aktualisierte Tabelle mit neuen Stunden
   - Neu berechnete Variationswarnungen
   - User lädt manuell ins Project Knowledge hoch

3. **COWORK_PROMPT

---

### Phase 2: Strukturierte Materialausarbeitung (Cowork)

**Trigger**: Cowork erhält Übergabeprotokoll + Cowork-Prompt

**Cowork-Ablauf (mit SKILL-PFLICHT-CHECK!):**

```
0. SKILL-PFLICHT-CHECK (NEU - VOR ALLEM ANDEREN!)
   ├── Welche Dateitypen werden erstellt?
   ├── .docx → arbeitsblatt-erstellen-v3 SKILL.md LESEN
   ├── .pptx → unterrichtsstunde-erstellen-v3 SKILL.md LESEN
   └── Bilder → unterrichts-medien SKILL.md LESEN

1. SKILLS LESEN (PFLICHT!)
   ├── /mnt/skills/user/arbeitsblatt-erstellen-v3/SKILL.md
   ├── /mnt/skills/user/unterrichtsstunde-erstellen-v3/SKILL.md
   └── (weitere je nach Bedarf)

2. COMFYUI STARTEN (wenn Bilder benötigt)
   ├── open -a "ComfyUI"
   └── Warten auf Server (curl check)

3. PRO STUNDE ABARBEITEN:
   ├── 3a. Arbeitsblätter erstellen (MIT VORLAGE!)
   │   ├── Vorlage_Fach.docx LADEN (NICHT Document()!)
   │   ├── ALLE Platzhalter ersetzen
   │   ├── Inhalt aus Protokoll einfügen
   │   ├── Validieren (Platzhalter, Umlaute)
   │   └── Speichern
   │
   ├── 3b. Bilder generieren
   │   ├── ComfyUI aufrufen (mcp__comfyui__generate_image)
   │   ├── Fallback: nanobanana → Hugging Face
   │   └── In Zielordner speichern
   │
   ├── 3c. PowerPoint erstellen (MIT VORLAGE/DESIGN-SYSTEM!)
   │   ├── Vorlage.pptx LADEN oder Design-System definieren
   │   ├── Folien gemäß Protokoll-Struktur
   │   ├── Timer-Videos einfügen
   │   ├── Generierte Bilder einfügen
   │   ├── Validieren
   │   └── Speichern
   │
   └── 3d. STUNDEN-CHECKLISTE ausfüllen ✓

4. COMFYUI SCHLIEßEN (wenn gestartet)
   └── osascript -e 'quit app "ComfyUI"'

5. NACH ALLEN STUNDEN:
   ├── Self-Assessment erstellen
   ├── Vokabelliste (nur Englisch)
   └── Abschluss-Report
```

---

## Skill Dependencies (v3!)

| Skill | Pfad | Funktion | Trigger |
|-------|------|----------|---------|
| **arbeitsblatt-erstellen-v3** | `/mnt/skills/user/arbeitsblatt-erstellen-v3/` | ALLE .docx für Unterricht | Arbeitsblätter, Infoblätter, Country Profiles, Crisis Briefings, Notes, Matrix, Phrases |
| **unterrichtsstunde-erstellen-v3** | `/mnt/skills/user/unterrichtsstunde-erstellen-v3/` | ALLE .pptx für Unterricht | Session PPTs, Simulation Slides, Workshop Präsentationen |
| **methoden-bibliothek** | `/mnt/skills/user/methoden-bibliothek/` | 48 Methoden, Alternativen finden | Bei Methodenwahl |
| **vokabeln-zusammenfassen** | `/mnt/skills/user/vokabeln-zusammenfassen/` | Vocabulary Sheets (nur Englisch) | Englisch-Stunden |
| **unterrichts-medien** | `/mnt/skills/user/unterrichts-medien/` | Bildgenerierung | Bilder für Materialien |

---

## HANDOVER-TEMPLATE ERGÄNZUNG (v5)

Das Übergabeprotokoll MUSS jetzt enthalten:

```markdown
## PFLICHT-SKILLS FÜR DIESE EINHEIT

| Dateityp | Skill | Vorlage |
|----------|-------|---------|
| .docx | arbeitsblatt-erstellen-v3 | Vorlage_Fach.docx |
| .pptx | unterrichtsstunde-erstellen-v3 | Vorlage.pptx oder Design-System |
| Bilder | unterrichts-medien | ComfyUI / Fallbacks |

⚠️ NIEMALS eigene Scripts von Grund auf erstellen!
⚠️ IMMER zuerst die Skills lesen und Vorlagen laden!
```

---

## Was dieser Skill IMMER gewährleistet

- ✅ **Roter Faden** durch Story-Check validiert
- ✅ **Sequentielle Planung** - eine Stunde komplett vor der nächsten
- ✅ **Textformate** explizit abgefragt
- ✅ **Methoden-Variation** durch Historie + Bibliothek
- ✅ **ComfyUI-Automation** für Bildgenerierung
- ✅ **Klare Trennung** Chat (Planung) ↔ Cowork (Ausführung)
- ✅ **Fertige Texte** im Handover (nicht nur Stichpunkte)
- ✅ **Encoding** (Umlaute) wird geprüft
- ✅ **Platzhalter** werden vollständig ersetzt
- ✅ **SKILL-PFLICHT-CHECK** verhindert eigene Scripts statt Vorlagen (NEU!)

---

## Error Prevention

### Häufige Fehler (VERMEIDEN!):

1. **Stunden nur "umrissen"**:
   → Story-Check PFLICHT, sequentielle Planung!

2. **Textformat nicht passend**:
   → Textformat-Abfrage bei jeder Textgenerierung!

3. **Methoden-Wiederholung**:
   → methoden-historie.md lesen, Variationsformel anwenden!

4. **Platzhalter nicht ersetzt**:
   → VALIDIERUNG nach jedem Dokument!

5. **Umlaute als ae/oe/ue**:
   → IMMER echte Umlaute, Validierung prüfen

6. **ComfyUI nicht gestartet/geschlossen**:
   → Automatischer Workflow in Cowork!

7. **Skills nicht gelesen**:
   → IMMER zuerst Skills lesen vor Materialerstellung!

8. **EIGENE SCRIPTS STATT VORLAGEN** (NEU - KRITISCH!):
   → SKILL-PFLICHT-CHECK vor jeder Datei-Erstellung!
   → Trigger erweitert in v3-Skills!
   → Handover listet explizit die zu verwendenden Skills!

---

## Version History

| Version | Datum | Änderungen |
|---------|-------|------------|
| 1.0 | 2025-01 | Initial creation |
| 2.0 | 18.01.2025 | HANDOVER_TEMPLATE + SELF_ASSESSMENT Templates |
| 3.0 | 18.01.2025 | COWORK_PROMPT + STUNDEN_CHECKLISTE, Encoding-Regeln |
| 4.0 | 24.01.2025 | 5 Kernprinzipien, Methoden-Tracking mit methoden-bibliothek, ComfyUI-Automation, v2-Skill-Referenzen |
| 5.0 | 27.01.2026 | 6. Kernprinzip: SKILL-PFLICHT-CHECK, v3-Skill-Referenzen |
| **5.1** | **29.01.2026** | **PHASE 2 TRIGGER: "Übergabeprotokoll", "Handover", "für Cowork" → automatisches Skill-Loading, Erkennungsmerkmale für Handover-Dokumente** |
