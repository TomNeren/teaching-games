# Schicksalswege — Entscheidungssystem Index

## Übersicht

Ein generationales Geschichtsspiel, das vier Familien durch das Deutsche Kaiserreich (1871-1918), die Weimarer Republik (1918-1933) und darüber hinaus begleitet.

---

## Die vier Familien

| Familie | Klasse | Zentrale Frage | Start-Ort |
|---------|--------|----------------|-----------|
| 🔴 **Schumann** | Arbeiter | Bildung → Politisierung → Revolution? | Sachsen/Chemnitz |
| 🔵 **Hoffmann** | Bürger | Ehe oder Emanzipation? | Leipzig |
| 🟡 **Goldstein** | Jüdisch | Assimilieren oder Bewahren? | Posen/Berlin |
| 🟣 **von Tresckow** | Adel | Tradition oder Modernisierung? | Brandenburg |

---

## Zeitstruktur

### Generation 1: 1871-1890 (Bismarck-Ära)
- Reichsgründung und Konsolidierung
- Sozialistengesetz (1878-1890)
- Kulturkampf
- Sozialversicherung

### Generation 2: 1890-1914 (Wilhelminische Ära)
- Neuer Kurs
- Massenparteien
- Frauenbewegung
- Weg in den Krieg

### Generation 3: 1914-1933 (Krieg und Republik)
- Erster Weltkrieg
- Revolution 1918
- Weimarer Republik
- Aufstieg des Nationalsozialismus

---

## Dokumenten-Struktur

```
entscheidungen/
├── README.md           # System-Übersicht
├── VARIABLEN.md        # 6 Attribute + Flags
├── KREUZUNGEN.md       # Familien-Interaktionen
├── INDEX.md            # Diese Datei
│
├── arbeiter/
│   ├── STORYLINE.md              # Gen 1 Übersicht
│   ├── 1871-1880-szenen.md       # Detaillierte Szenen
│   ├── 1881-1890-szenen.md
│   ├── 1890-1914-generation2.md  # Gen 2
│   └── KONSEQUENZEN.md           # Langzeitfolgen
│
├── buerger/
│   ├── BIOGRAFIEN.md             # 15 Quell-Biografien
│   └── STORYLINE.md              # Gen 1 Übersicht
│
├── juedisch/
│   └── STORYLINE.md              # Gen 1 + Assimilations-Mechanik
│
└── adel/
    └── STORYLINE.md              # Gen 1 + Ehre/Schulden-Mechanik
```

---

## Schlüssel-Entscheidungspunkte

### 1871-1890

| Jahr | Arbeiter | Bürger | Jüdisch | Adel |
|------|----------|--------|---------|------|
| 1871 | Stadt oder Land? | Höhere Töchterschule | Emanzipation — Hoffnung | Militär oder Gut? |
| 1873 | Gründerkrach: Streikbrecher? | Ruin oder Überleben | Sündenbock-Mechanismus | Agrarkrise: Modernisieren? |
| 1875 | Bildungsverein? | — | Jüdisch oder christlich heiraten? | — |
| 1876 | Heirat | Ball/Partnerwahl | Beschneidung? | Mesalliance? |
| 1878 | Sozialistengesetz: Untergrund? | Dienstmädchen-Ethik | Antisemitismusstreit | Schutzzölle |
| 1880 | Kindererziehung | Frauenbewegung? | Antisemiten-Petition | Offizierslaufbahn für Sohn? |

### 1890-1914

| Jahr | Arbeiter | Bürger | Jüdisch | Adel |
|------|----------|--------|---------|------|
| 1890 | SPD legal: Triumphale Rückkehr? | — | — | Bismarcks Sturz |
| 1893 | Berufswahl der Kinder | — | — | — |
| 1900 | Jahrhundertwende | Studium für Tochter? | — | — |
| 1905 | Revolution Russland: Massenstreik? | — | — | — |
| 1912 | SPD stärkste Fraktion | Frauenstimmrecht? | Zionismus? | — |
| **1914** | **BURGFRIEDEN** | Söhne im Krieg | Patriotismus beweisen? | Ehre im Krieg |

### 1914-1933

| Jahr | Alle Familien |
|------|---------------|
| 1918 | Revolution: Welche Seite? |
| 1919 | Weimarer Republik: Akzeptieren? |
| 1923 | Hyperinflation: Überleben? |
| 1929 | Weltwirtschaftskrise |
| 1933 | Machtergreifung: Fliehen, Anpassen, Widerstand? |

---

## Spielmechanik

### 6 Grundattribute
- **Bildung** — Wissen, Lesen, Selbstbildung
- **Vermögen** — Geld, Besitz, wirtschaftliche Sicherheit
- **Politik** — Politische Position (-100 reaktionär bis +100 revolutionär)
- **Gesundheit** — Körperliche Verfassung
- **Ansehen** — Sozialer Status, Respekt
- **Solidarität** — Netzwerk, Gemeinschaft

### Spezial-Mechaniken pro Familie
| Familie | Spezial-Mechanik |
|---------|------------------|
| Arbeiter | — (Standardmechanik) |
| Bürger | Freiheits-Meter (unsichtbar) |
| Jüdisch | Assimilations-Meter + Sichtbarkeits-Meter |
| Adel | Ehre-Meter + Schulden-Meter |

### Generationen-Vererbung
```
Kind.Attribut = (Mutter + Vater) / 4 + Kindheitserfahrungen
```

### Narrative Vererbung
- Geschichten, die das Kind gehört hat
- Flags (z.B. "Vater war Streikbrecher")
- Trauma und Stolz vererben sich

---

## Biografische Quellen

### Arbeiter (6 Volltexte)
- Moritz Bromme — Fabrikarbeiter
- Ottilie Baader — Näherin/SPD
- Adelheid Popp — Fabrikarbeiterin
- Doris Viersbeck — Dienstmädchen
- Franz Bergg — Kellner/Seemann
- Franz Rehbein — Landarbeiter

### Bürger (15 Biografien aus Schraut)
- Hedwig Heyl — Muster-Bürgerin
- Hedwig Dohm — Radikale Feministin
- Franziska Tiburtius — Erste Ärztin
- Margarete Steiff — Unternehmerin
- Margarethe Krupp — Industriellen-Gattin
- u.a.

### Jüdisch
- Walther Rathenau — Industrieller
- Hedwig Dohm — Assimilierte Familie
- Auguste Hauschner — Prager Jüdin

### Adel
- Lily Braun — Vom Adel zur SPD
- (Mehr Quellen nötig)

---

## Kreuzungspunkte

Die Familien begegnen sich:
1. **Herr/Diener** — Schumann-Schwester arbeitet bei Hoffmann
2. **Händler** — Goldstein verkauft an Hoffmann
3. **Landarbeit** — Schumann auf von Tresckow-Gut
4. **Mesalliance** — Standesübergreifende Heirat möglich
5. **Revolution 1918** — Alle Familien, verschiedene Seiten

---

## Status

| Komponente | Status |
|------------|--------|
| Arbeiter Gen 1 | ✅ Fertig |
| Arbeiter Gen 2 | ✅ Fertig |
| Arbeiter Gen 3 | ⏳ Geplant |
| Bürger Gen 1 | ✅ Fertig |
| Bürger Gen 2 | ⏳ Geplant |
| Jüdisch Gen 1 | ✅ Fertig |
| Jüdisch Gen 2 | ⏳ Geplant |
| Adel Gen 1 | ✅ Fertig |
| Adel Gen 2 | ⏳ Geplant |
| Kreuzungen | ✅ Konzept fertig |
| Historische Ereignisse | ✅ 1871-1890 detailliert |

---

## Nächste Schritte

1. Generation 2 für Bürger, Jüdisch, Adel
2. Generation 3 für alle Familien
3. Mehr detaillierte Szenen
4. Integration historischer Bilder
5. Spielbare Prototyp-Version
