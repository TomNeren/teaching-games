# Mammutprojekt v2: Generationales Geschichtsspiel
## "Schicksalswege" — Ein interaktives Spiel durch die deutsche Geschichte

**Stand:** 2026-02-07  
**Status:** Konzeptphase

---

## 1. Vision

Ein entscheidungsbasiertes Spiel, in dem Schüler:innen eine Familie über mehrere Generationen durch die deutsche Geschichte begleiten — von der Reichsgründung 1871 bis zur Wiedervereinigung 1990.

**Kern-Idee:** Nicht Geschichte lernen, sondern Geschichte *erleben*. Jede Entscheidung hat Konsequenzen, die sich über Generationen auswirken.

---

## 2. Spielmechanik

### 2.1 Zeitstruktur
- **Start:** 1871 (Reichsgründung)
- **Wendepunkte:** 1878, 1888, 1890, 1900, 1914, 1918, 1933, 1945, 1949, 1961, 1989
- **Ende:** 1990 (Wiedervereinigung)

### 2.2 Perspektiven (wählbar)
| Perspektive | Startmilieu | Kernspannungen |
|-------------|-------------|----------------|
| **Arbeiterfamilie** | Berliner Mietskaserne | Armut vs. Aufstieg, SPD vs. Staat |
| **Bürgerfamilie** | Bildungsbürgertum, Kleinstadt | Tradition vs. Moderne, Assimilation |
| **Adelsfamilie** | Ostelbisches Gut | Machtverlust, Militär, Ehre |
| **Jüdische Familie** | Händler/Akademiker | Integration vs. Antisemitismus |

### 2.3 Generationenprinzip
- Spieler:in trifft Entscheidungen für aktuellen Protagonisten
- Bei Zeitsprung: Kinder/Enkel übernehmen
- Konsequenzen vererben sich (Vermögen, Bildung, politische Haltung, Trauma)

---

## 3. Historische Fundierung

### 3.1 Vorhandene Quellen
| Quelle | Autor | Zeitraum | Stärke |
|--------|-------|----------|--------|
| `wirsching-deutsche-geschichte-20jh.txt` | Wirsching | 1900-1990 | ⭐ Sonderweg-Debatte, Kaiserreich-Überblick |
| `winkler-langer-weg-band2.txt` | Winkler | 1933-1990 | NS-Zeit, Nachkrieg detailliert |
| `fischer-weltgeschichte-35-nachkrieg.txt` | Benz/Graml | 1945-1982 | Blockbildung, Kalter Krieg |
| `lemo-kaiserreich-alltag.md` | LeMO/DHM | 1871-1918 | Alltagsdetails, Sozialgeschichte |
| `feminism-revolution-atwood.pdf` | — | 19./20. Jh. | Frauenbewegung, Arbeiterbewegung |

### 3.2 Fehlende Quellen (Recherche nötig)
- [ ] **Winkler Band I** (Kaiserreich + Weimar)
- [ ] Biografien "einfacher Leute" aus dem Kaiserreich
- [ ] Alltagsgeschichte Weimarer Republik
- [ ] Oral History / Zeitzeugenberichte

### 3.3 Empfohlene Ergänzungen
- **Günther Drommer: "Im Kaiserreich"** — 39 Biografien (Perlentaucher-Fund)
- **Ritter/Tenfelde: "Arbeiter im Deutschen Kaiserreich 1871-1914"**
- **Jürgen Schmidt: "August Bebel. Kaiser der Arbeiter"** — Arbeiterfigur

---

## 4. Kaiserreich-Modul (1871-1914) — Detailkonzept

### 4.1 Gesellschaftliche Spannungen (aus Wirsching + LeMO)

**"Übergangsmenschen"** — die wilhelminische Generation:
> "Innerhalb weniger Jahrzehnte erfolgte der Übergang vom Agrarstaat zum Industriestaat; innerhalb eines Menschenalters veränderten sich Landschaft, Arbeitswelt, soziale Beziehungen, moralische Bindungen, politische Konstellationen."

**Spielbare Konflikte:**
1. **Tradition vs. Moderne** — Elektrizität, Telefon, Automobile verändern alles
2. **Adel vs. Bürgertum** — Wer hat die Macht?
3. **Stadt vs. Land** — Landflucht, Urbanisierung
4. **Untertanengeist vs. Emanzipation** — SPD wächst, aber Kaiserbild an der Wand
5. **Nation vs. Klasse** — Was bindet die Gesellschaft?

### 4.2 Mögliche Entscheidungspunkte

**1871-1878: Gründerzeit**
- Ziehst du in die Stadt oder bleibst du auf dem Land?
- Investierst du in neue Technik oder bleibst du beim Bewährten?
- Schließt du dich der Arbeiterbewegung an?

**1878-1890: Sozialistengesetze**
- Gehst du zu verbotenen SPD-Treffen?
- Verrätst du Genossen für Karrierevorteile?
- Nutzt du die neuen Sozialgesetze (Kranken-, Unfall-, Rentenversicherung)?

**1890-1914: Wilhelminische Ära**
- Strebst du das Reserveoffizierspatent an?
- Lässt du deinen Sohn studieren oder in die Lehre gehen?
- Wie reagierst du auf wachsenden Antisemitismus?

### 4.3 Authentische Details (aus LeMO)
- 1881: Erste elektrische Straßenbahn in Berlin
- 1881: Erste Telefonvermittlungen
- 1895-1913: Hochkonjunktur, aber Lebensmittel +33% teurer
- 1912: SPD wird stärkste Reichstagsfraktion (34,8%)
- 1914: 10% der Haushalte haben Strom
- Lebenserwartung steigt von 37 (1871) auf 47 Jahre (1910)

---

## 5. Technische Umsetzung

### 5.1 Format
- **HTML/JavaScript** — browserbasiert, kein Download
- **Twine-artig** — Entscheidungsbaum mit Variablen
- **Responsive** — funktioniert auf Schul-iPads

### 5.2 Assets
- **Bilder:** Hugging Face generiert (historisch anmutend)
- **Audio:** Bark TTS für Erzählung (optional)
- **Musik:** Suno-generierte Stücke (bereits vorhanden)
- **Schrift:** Fraktur für Zeitdokumente, moderne Schrift für UI

### 5.3 Tracking
- Entscheidungen werden gespeichert
- Familienbaum visualisiert
- "Vermächtnis-Score" am Ende (Was hat deine Familie erreicht/erlitten?)

---

## 6. Pädagogische Ziele

### 6.1 Lernziele
1. **Multiperspektivität** — Geschichte aus verschiedenen Blickwinkeln verstehen
2. **Kontingenz** — Geschichte ist nicht vorherbestimmt, Entscheidungen zählen
3. **Empathie** — Sich in historische Akteure hineinversetzen
4. **Strukturwissen** — Große Zusammenhänge (Industrialisierung, Kriege, Demokratie)

### 6.2 Reflexionsebene
- Nach jedem Kapitel: "Was wäre wenn...?"-Fragen
- Vergleich mit Mitschüler:innen (andere Entscheidungen, andere Schicksale)
- Historische Einordnung durch Lehrkraft

---

## 7. Nächste Schritte

### Sofort (diese Woche)
- [x] Quellensammlung aufbauen
- [ ] Biografien recherchieren (Drommer, Bebel, etc.)
- [ ] Ersten Prototyp Kaiserreich-Modul (1871-1890)

### Kurzfristig
- [ ] Winkler Band I beschaffen
- [ ] Alltagsdetails aus Quellen extrahieren
- [ ] UI-Mockup erstellen

### Mittelfristig
- [ ] Alle Epochen-Module konzipieren
- [ ] Playtest mit Schüler:innen
- [ ] Bilder generieren

---

## Anhang: Offene Fragen

1. **Welche Klasse soll das zuerst testen?** (BG? AV? Berufskolleg?)
2. **Wie lange pro Modul?** (1 Doppelstunde? Mehrere Sitzungen?)
3. **Sollen alle Perspektiven verfügbar sein oder nur eine pro Durchgang?**
4. **Lokaler Bezug?** (Lörrach/Freiburg statt Berlin? Oder beides?)
