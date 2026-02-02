# Mammutprojekt: Interaktive NS-Simulation
## "Entscheidungen 1933-1945"

---

## 🎯 Vision

Eine interaktive, entscheidungsbasierte Simulation, die Schüler durch die NS-Zeit führt — aus **drei Perspektiven**:
- 👤 **Opfer** (jüdische Familie, politischer Verfolgter)
- 😐 **Zuschauer** (gewöhnlicher Bürger — Mitläufer oder stiller Widerstand?)
- 👔 **Täter/Funktionsträger** (Beamter, Lehrer — wie weit geht man mit?)

**Kernmechanik:** Entscheidungen haben Konsequenzen. Alternative Handlungspfade. Historisch fundiert.

---

## 📊 Recherche: Was existiert bereits?

### Kommerzielle Spiele

| Titel | Beschreibung | Nutzbar? |
|-------|--------------|----------|
| **Through the Darkest of Times** | Widerstandsgruppe in Berlin 1933-45 managen | ✅ Inspiration für Mechanik |
| **My Child Lebensborn** | Nachkriegs-Norwegen, Stigmatisierung | ✅ Emotionale Tiefe |
| **Attentat 1942** | Tschechische Resistance, Zeitzeugen-Interviews | ✅ Dokumentar-Stil |
| **The Light in the Darkness** | Kindertransport-Geschichte | ✅ Narrative Struktur |

### Akademische Projekte

| Projekt | Institution | Ansatz |
|---------|-------------|--------|
| **Interact** | USC Shoah Foundation | VR-Gespräche mit Holocaust-Überlebenden |
| **Witness: Auschwitz** | — | VR-Erfahrung (umstritten) |
| **Rosenstrasse TRPG** | — | Tabletop-Rollenspiel zum Widerstand |

### Erkenntnisse für unser Projekt

✅ **Was funktioniert:**
- Entscheidungen ohne "richtige" Lösung
- Historische Genauigkeit + emotionale Tiefe
- Fokus auf Alltag, nicht nur Extreme
- Keine "Gewinn"-Bedingung — Geschichte ist nicht zu "gewinnen"

❌ **Was vermieden werden sollte:**
- Gamification von Leiden
- Realistische Gewaltdarstellung
- Vereinfachte Gut/Böse-Dichotomie
- "Befreiung" als Spielziel

---

## 🏗️ Technische Architektur

### Option A: Web-basiert (empfohlen)
```
┌─────────────────────────────────────────────────┐
│                   Frontend                       │
│  HTML/CSS/JS — Responsive, funktioniert überall │
└─────────────────────────────────────────────────┘
                        │
         ┌──────────────┼──────────────┐
         ▼              ▼              ▼
    ┌─────────┐   ┌──────────┐   ┌──────────┐
    │  Twine  │   │  Ink     │   │  Custom  │
    │ Engine  │   │ (Inkle)  │   │   JS     │
    └─────────┘   └──────────┘   └──────────┘
         │              │              │
         └──────────────┼──────────────┘
                        ▼
              ┌──────────────────┐
              │  Story-Datenbank │
              │  (JSON/Markdown) │
              └──────────────────┘
```

### Framework-Vergleich

| Framework | Vorteile | Nachteile |
|-----------|----------|-----------|
| **Twine** | Einfach, visueller Editor, kostenlos | Begrenzte Komplexität |
| **Ink (Inkle)** | Mächtige Scripting-Sprache, Unity-Integration | Lernkurve |
| **Ren'Py** | Visual Novel Engine, Python-basiert | Eher für VN-Stil |
| **Custom (React/Vue)** | Volle Kontrolle | Mehr Entwicklungsaufwand |

**Empfehlung:** Start mit **Twine** für Prototyp, dann ggf. Migration zu Ink/Custom.

---

## 🖼️ Bildgenerierung

### MCP-Optionen

```bash
# Replicate (FLUX-Modell) — empfohlen
mcporter config add imagegen \
  --command "npx -y @gongrzhe/image-gen-server" \
  --env "REPLICATE_API_TOKEN=xxx"

# DALL-E (OpenAI)
mcporter config add dalle \
  --command "npx -y @fastmcp-me/imagegen-mcp" \
  --env "OPENAI_API_KEY=xxx"
```

### Ethische Leitlinien für Bilder

✅ **Generieren:**
- Historische Straßenszenen (neutral)
- Dokumente, Ausweise, Zeitungen
- Symbolische Darstellungen
- Architektur der Zeit

❌ **NICHT generieren:**
- Gewalt, Leid, Deportationen
- KZ-Szenen
- Erniedrigende Darstellungen
- Propagandamaterial ohne Kontext

**Lösung:** Mix aus generierten neutralen Bildern + historischen Public-Domain-Fotos

---

## 🔊 Text-to-Speech

OpenClaw hat native TTS-Unterstützung:
```bash
# Beispiel
tts "Du stehst am Bahnhof. Ein Zug fährt ein..."
```

**Einsatz:**
- Erzählerstimme für Szenen
- Historische Zitate vorlesen
- Optional: verschiedene Stimmen für Charaktere

---

## 📖 Narrative Struktur

### Die drei Perspektiven

```
                    ┌─────────────────────┐
                    │    PROLOG: 1933     │
                    │   Machtergreifung   │
                    └──────────┬──────────┘
                               │
         ┌─────────────────────┼─────────────────────┐
         ▼                     ▼                     ▼
   ┌───────────┐         ┌───────────┐         ┌───────────┐
   │  OPFER    │         │ ZUSCHAUER │         │   TÄTER   │
   │  Familie  │         │  Bürger   │         │  Beamter  │
   │  Goldstein│         │  Müller   │         │  Schmidt  │
   └─────┬─────┘         └─────┬─────┘         └─────┬─────┘
         │                     │                     │
    [Entscheidungen]     [Entscheidungen]     [Entscheidungen]
         │                     │                     │
         ▼                     ▼                     ▼
   ┌───────────┐         ┌───────────┐         ┌───────────┐
   │ 1935:     │         │ 1935:     │         │ 1935:     │
   │ Nürnberg  │         │ Nachbar   │         │ Dienst-   │
   │ Gesetze   │         │ verliert  │         │ anweisung │
   └─────┬─────┘         │ Geschäft  │         └─────┬─────┘
         │               └─────┬─────┘               │
         ▼                     ▼                     ▼
        ...                   ...                   ...
         │                     │                     │
         └─────────────────────┼─────────────────────┘
                               ▼
                    ┌─────────────────────┐
                    │   EPILOG: 1945+     │
                    │  Was wurde aus...?  │
                    └─────────────────────┘
```

### Beispiel-Entscheidungspunkt (Zuschauer-Perspektive)

```
═══════════════════════════════════════════════════════
NOVEMBER 1938 — Die Nacht

Du wachst auf. Draußen ist Lärm. Glas splittert.
Du schaust aus dem Fenster: Das Geschäft der Familie 
Rosenthal gegenüber brennt. Menschen stehen herum.
Einige schauen zu, andere machen mit.

Was tust du?

[A] Du bleibst drinnen. Es ist gefährlich.
[B] Du gehst raus, um zu sehen was passiert.
[C] Du versuchst, den Rosenthals zu helfen.
[D] Du rufst die Polizei an.
═══════════════════════════════════════════════════════
```

Jede Entscheidung hat Konsequenzen — und keine ist "richtig".

---

## 🗃️ Wissensintegration

### Akademische Quellen (via OpenAlex, ERIC)
```bash
/root/.openclaw/tools/research "bystander effect Nazi Germany" -n 5
```

### Historische Fakten-Datenbank
- Zeitleiste der Gesetze und Ereignisse
- Biografien realer Menschen
- Statistiken und Zahlen
- Primärquellen (Tagebücher, Briefe)

### Verknüpfung mit Tismaneanu
Das Buch liefert theoretischen Rahmen:
- Ideologische Mechanismen
- "Banalität des Bösen"
- Schrittweise Radikalisierung

---

## 📅 Entwicklungsplan

### Phase 1: Konzept & Prototyp (2-4 Wochen)
- [ ] Narrative-Design: Hauptstränge ausarbeiten
- [ ] Twine-Prototyp mit 1 Perspektive
- [ ] Erste Entscheidungsbäume
- [ ] Test mit kleiner Gruppe

### Phase 2: Erweiterung (4-6 Wochen)
- [ ] Alle drei Perspektiven
- [ ] Bildgenerierung einbinden
- [ ] TTS-Erzählung
- [ ] Historische Dokumente einbetten

### Phase 3: Verfeinerung (2-4 Wochen)
- [ ] Feedback einarbeiten
- [ ] Pädagogische Begleitmaterialien
- [ ] Lehrerhandreichung
- [ ] Hosting & Distribution

### Phase 4: Evaluation
- [ ] Pilottest in Klassen
- [ ] Feedback sammeln
- [ ] Iteration

---

## ⚠️ Ethische Leitlinien

### Yad Vashem Prinzipien
1. Individuen, nicht Zahlen
2. Historische Genauigkeit
3. Keine Vereinfachung
4. Würde der Opfer wahren
5. Kontext vor Schock

### Unsere Zusatz-Regeln
- Kein "Spielen" von Tätern ohne kritische Reflexion
- Immer Ausstiegsmöglichkeit / Pausenfunktion
- Nachbesprechung ist Pflicht
- Trigger-Warnungen wo nötig
- Keine Punkte, keine Highscores, kein "Gewinnen"

---

## 🛠️ Nächste Schritte

1. **Bildgenerierung einrichten** — Replicate API-Key besorgen
2. **Twine installieren** — Prototyp-Umgebung aufsetzen  
3. **Narrative schreiben** — Mit Zuschauer-Perspektive beginnen
4. **Historische Recherche** — Alltagsszenen 1933-1945 sammeln

---

## 💬 Offene Fragen an Tom

1. Welche Perspektive soll zuerst entwickelt werden?
2. Soll es nur auf Deutsch sein oder auch Englisch?
3. Wie viel Spielzeit pro Durchgang? (30 Min? 60 Min? 90 Min?)
4. Klassenstufe / Alter der Zielgruppe?
5. Soll es offline funktionieren (USB-Stick) oder online?

---

*Erstellt von Aether ✨ | Mammutprojekt für Tom | Berufliche Schule Lörrach*
