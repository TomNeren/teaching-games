---
name: unterrichtsplanung-workflow
description: Strukturierter 2-Phasen-Workflow für Unterrichtsplanung mit 5 Kernprinzipien - Roter Faden (Story-Telling), Hybrid Chat/Cowork, Textformat-Abfrage, Sequentielle Planung, ComfyUI-Automation. Enthält HANDOVER_TEMPLATE, COWORK_PROMPT, STUNDEN_CHECKLISTE und METHODEN_HISTORIE Templates.
---

# Unterrichtsplanung Workflow Skill (v4.0)

**Version:** 4.0.0
**Stand:** 24.01.2025
**Changelog:** 5 Kernprinzipien, Methoden-Tracking mit methoden-bibliothek, ComfyUI-Automation, v2-Skill-Referenzen

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
    ├── METHODEN_HISTORIE_TEMPLATE.md     # NEU: Tracking vergangener Methoden
    ├── SELF_ASSESSMENT_DE.md             # Self-Assessment (Deutsch)
    └── SELF_ASSESSMENT_EN.md             # Self-Assessment (Englisch)
```

---

## ⚡ 5 KERNPRINZIPIEN (NEU in v4.0)

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
| Konzept entwickeln | Vorlagen laden |
| Roter Faden durchdenken | Platzhalter ersetzen |
| Methodenwahl (mit Variation) | Bilder generieren (ComfyUI) |
| **FERTIGE Arbeitsaufträge** schreiben | Timer einfügen |
| **FERTIGE AB-Texte** schreiben | PPT erstellen |
| Bild-Prompts formulieren | Dateien organisieren |
| Story-Check durchführen | Validierung ausführen |

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
comfyui:generate_image für jedes Bild

# 4. ComfyUI schließen
osascript -e 'quit app "ComfyUI"'
```

**Fallback-Kaskade:**
1. ComfyUI (lokal) → Beste Qualität
2. nanobanana:generate_image → Gemini-basiert
3. Hugging Face gr4_z_image_turbo_generate → Schnell

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

### Komponente 1: methoden-historie.md

**Speicherort:** Project Knowledge (pro Fach-Projekt)
**Template:** `/mnt/skills/user/unterrichtsplanung-workflow/templates/METHODEN_HISTORIE_TEMPLATE.md`

**Struktur:**
```markdown
# Methoden-Historie [Projektname]

## Letzte Verwendungen

| Datum | Stunde/Thema | Einstieg | Erarbeitung | Sicherung |
|-------|--------------|----------|-------------|-----------|
| 24.01 | Bewerbung 1 | Bildimpuls | Gruppenarbeit | Blitzlicht |
| 22.01 | Lebenslauf | Brainstorming | Think-Pair-Share | Galeriegang |
| 20.01 | Anschreiben | Bildimpuls | Einzelarbeit | Blitzlicht |

## Variationswarnung
- **Bildimpuls** (2x in letzten 3 Stunden) → ⚠️ Alternative wählen!
- **Blitzlicht** (2x in letzten 3 Stunden) → ⚠️ Alternative wählen!
```

---

### Komponente 2: methoden-bibliothek (für Alternativen)

**Skill:** `/mnt/skills/user/methoden-bibliothek/SKILL.md`

**Inhalt:**
- 15 Einstieg-Methoden (Bildimpuls, Zitat-Reaktion, Mini-Mystery, etc.)
- 18 Erarbeitungs-Methoden (Gruppenpuzzle, Gallery Walk, World Café, etc.)
- 15 Sicherungs-Methoden (Exit Ticket, 3-2-1, Concept Map, etc.)
- Sortiert nach: Zeitbedarf, Sozialform

**Wann konsultieren:**
- Wenn Methode gesperrt ist (3+ Verwendungen)
- Wenn Warnung vorliegt (2 Verwendungen)
- Wenn User nach neuen Ideen fragt
- Wenn spezifische Rahmenbedingungen gelten (Zeit, Sozialform)

---

### Variationsformel

| Verwendungen in Folge | Status | Aktion |
|----------------------|--------|--------|
| 1x | ✅ OK | Frei verwendbar |
| 2x | ⚠️ Warnung | Alternative aus methoden-bibliothek vorschlagen |
| 3x | 🔴 Gesperrt | NICHT mehr verwenden, Alternative PFLICHT |

---

### Workflow-Integration

```
┌─────────────────────────────────────────────────────────┐
│              PLANUNGSPROZESS START                      │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  1. methoden-historie.md LESEN (wenn vorhanden)         │
│     → Welche Methoden wurden zuletzt verwendet?         │
│     → Welche sind gesperrt (3+ Verwendungen)?           │
│     → Welche haben Warnung (2 Verwendungen)?            │
│                                                         │
│  2. Bei Methodenwahl: Variationsformel ANWENDEN         │
│                                                         │
│     ┌─────────────────────────────────────────────┐     │
│     │ Methode gesperrt oder Warnung?              │     │
│     │                                             │     │
│     │ JA → methoden-bibliothek konsultieren:      │     │
│     │      → Gleiche Phase (Einstieg/Erarb/Sich)  │     │
│     │      → Passender Zeitrahmen                 │     │
│     │      → Passende Sozialform                  │     │
│     │      → Alternative vorschlagen              │     │
│     │                                             │     │
│     │ NEIN → Methode frei verwendbar              │     │
│     └─────────────────────────────────────────────┘     │
│                                                         │
├─────────────────────────────────────────────────────────┤
│              PLANUNGSPROZESS ENDE                       │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  3. methoden-historie-update.md erstellen               │
│     → Neue Zeile mit Datum, Thema, Methoden             │
│     → Variationswarnungen neu berechnen                 │
│     → User lädt ins Project Knowledge hoch              │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

### Schnellreferenz: Alternativen nach Phase

**Wenn EINSTIEG gesperrt:**
| Gesperrt | Alternativen (ähnlich) |
|----------|------------------------|
| Bildimpuls | Zitat-Reaktion, Concept Cartoon, Video-Stopp |
| Brainstorming | Murmelphase, Stummes Schreibgespräch |
| Blitzlicht | Positionslinie, Vier-Ecken-Methode |
| Think-Pair-Share | Murmelphase, Warm-up Quiz |

**Wenn ERARBEITUNG gesperrt:**
| Gesperrt | Alternativen (ähnlich) |
|----------|------------------------|
| Gruppenarbeit | Placemat, Lerntempoduett, Partnerinterview |
| Think-Pair-Share | Kugellager, Murmelphase |
| Textarbeit/Einzelarbeit | Reziprokes Lesen, Lerntempoduett |
| Gallery Walk | World Café, Marktplatz der Ideen |

**Wenn SICHERUNG gesperrt:**
| Gesperrt | Alternativen (ähnlich) |
|----------|------------------------|
| Blitzlicht | Murmelgruppe, One-Minute-Paper |
| Exit Ticket | 3-2-1 Methode, Fünf-Finger-Feedback |
| Präsentation | Elevator Pitch, Quiz-Duell |
| Concept Map | Schneeballmethode, Lerntagebuch |

---

## ⚡ KRITISCHE REGELN (unverändert)

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

**Am Ende von Phase 1 erstellt Chat ZWEI Dokumente:**

1. **Übergabeprotokoll** (HANDOVER_TEMPLATE.md)
   - Vollständige Spezifikation aller Materialien
   - FERTIGE Texte (nicht nur Stichpunkte!)
   - PPT-Struktur Folie für Folie
   - Bild-Prompts

2. **methoden-historie-update.md** (für Project Knowledge)
   - Aktualisierte Tabelle mit neuen Stunden
   - Neu berechnete Variationswarnungen
   - User lädt manuell ins Project Knowledge hoch

---

### Phase 2: Strukturierte Materialausarbeitung (Cowork)

**Trigger**: Cowork erhält Übergabeprotokoll + Cowork-Prompt

**Cowork-Ablauf (mit ComfyUI-Automation):**

```
1. SKILLS LESEN (PFLICHT!)
   ├── /mnt/skills/user/arbeitsblatt-erstellen-v2/SKILL.md
   ├── /mnt/skills/user/unterrichtsstunde-erstellen-v2/SKILL.md
   └── (weitere je nach Bedarf)

2. COMFYUI STARTEN
   ├── open -a "ComfyUI"
   └── Warten auf Server (curl check)

3. PRO STUNDE ABARBEITEN:
   ├── 3a. Arbeitsblätter erstellen
   │   ├── Vorlage laden
   │   ├── ALLE Platzhalter ersetzen
   │   ├── Inhalt aus Protokoll einfügen
   │   ├── Validieren (Platzhalter, Umlaute)
   │   └── Speichern
   │
   ├── 3b. Bilder generieren
   │   ├── ComfyUI aufrufen (comfyui:generate_image)
   │   ├── Fallback: nanobanana → Hugging Face
   │   └── In Zielordner speichern
   │
   ├── 3c. PowerPoint erstellen
   │   ├── Vorlage laden
   │   ├── Folien gemäß Protokoll-Struktur
   │   ├── Timer-Videos einfügen
   │   ├── Generierte Bilder einfügen
   │   ├── Validieren
   │   └── Speichern
   │
   └── 3d. STUNDEN-CHECKLISTE ausfüllen ✓

4. COMFYUI SCHLIEßEN
   └── osascript -e 'quit app "ComfyUI"'

5. NACH ALLEN STUNDEN:
   ├── Self-Assessment erstellen
   ├── Vokabelliste (nur Englisch)
   └── Abschluss-Report
```

---

## Skill Dependencies (v2!)

| Skill | Pfad | Funktion |
|-------|------|----------|
| **arbeitsblatt-erstellen-v2** | `/mnt/skills/user/arbeitsblatt-erstellen-v2/` | DOCX mit bereinigten Vorlagen |
| **unterrichtsstunde-erstellen-v2** | `/mnt/skills/user/unterrichtsstunde-erstellen-v2/` | PPTX mit Video-Timern |
| **methoden-bibliothek** | `/mnt/skills/user/methoden-bibliothek/` | 48 Methoden, Alternativen finden |
| **vokabeln-zusammenfassen** | `/mnt/skills/user/vokabeln-zusammenfassen/` | Vocabulary Sheets (nur Englisch) |
| **unterrichts-medien** | `/mnt/skills/user/unterrichts-medien/` | Bildgenerierung (Fallback) |

---

## Templates

### 1. HANDOVER_TEMPLATE.md
Vollständiges Übergabeprotokoll mit fertigen Texten.
→ Siehe `/mnt/skills/user/unterrichtsplanung-workflow/templates/HANDOVER_TEMPLATE.md`

### 2. COWORK_PROMPT.md
Ausführungsanweisung für Cowork mit ComfyUI-Automation.
→ Siehe `/mnt/skills/user/unterrichtsplanung-workflow/templates/COWORK_PROMPT.md`

### 3. STUNDEN_CHECKLISTE.md
Validierungs-Checkliste nach jeder Stunde.
→ Siehe `/mnt/skills/user/unterrichtsplanung-workflow/templates/STUNDEN_CHECKLISTE.md`

### 4. METHODEN_HISTORIE_TEMPLATE.md (NEU!)
Vorlage für das Methoden-Tracking in Project Knowledge.
→ Siehe `/mnt/skills/user/unterrichtsplanung-workflow/templates/METHODEN_HISTORIE_TEMPLATE.md`

### 5. SELF_ASSESSMENT_DE.md / SELF_ASSESSMENT_EN.md
Self-Assessment Templates für beide Sprachen.
→ Siehe `/mnt/skills/user/unterrichtsplanung-workflow/templates/`

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

---

## Version History

| Version | Datum | Änderungen |
|---------|-------|------------|
| 1.0 | 2025-01 | Initial creation |
| 2.0 | 18.01.2025 | HANDOVER_TEMPLATE + SELF_ASSESSMENT Templates |
| 3.0 | 18.01.2025 | COWORK_PROMPT + STUNDEN_CHECKLISTE, Encoding-Regeln |
| **4.0** | **24.01.2025** | **5 Kernprinzipien, Methoden-Tracking mit methoden-bibliothek, ComfyUI-Automation, v2-Skill-Referenzen** |
