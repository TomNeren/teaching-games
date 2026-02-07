# Variablen-System

## Persönliche Attribute

### Bildung (-100 bis +100)
```
-100: Analphabet, keinerlei Schulbildung
 -50: Wenige Jahre Volksschule, kaum lesen
   0: Volksschulabschluss (Standard)
 +25: Selbststudium, Arbeiterbildungsverein
 +50: Fortbildung, gutes Allgemeinwissen
 +75: Gymnasialbildung oder äquivalent
+100: Akademische Bildung
```

**Beeinflusst:**
- Berufsmöglichkeiten
- Politisches Bewusstsein
- Aufstiegschancen der Kinder
- Zugang zu Informationen

### Vermögen (-100 bis +100)
```
-100: Verschuldet, Pfändung droht
 -50: Leben von der Hand in den Mund
   0: Gerade so über die Runden
 +25: Kleine Ersparnisse
 +50: Bescheidener Wohlstand
 +75: Vermögend
+100: Reich
```

**Beeinflusst:**
- Krisenfestigkeit
- Heiratschancen
- Wohnqualität
- Gesundheit (bessere Ernährung, Arzt)
- Bildung der Kinder

### Politik (-100 bis +100)
```
-100: Reaktionär, kaisertreu
 -50: Konservativ
 -25: Unpolitisch-angepasst
   0: Unpolitisch-neutral
 +25: Liberal, reformorientiert
 +50: Sozialdemokratisch
 +75: Radikal links
+100: Revolutionär/kommunistisch
```

**Beeinflusst:**
- Risiko bei Repression (Sozialistengesetz)
- Netzwerk in der Bewegung
- Weltanschauung
- Reaktion auf historische Ereignisse
- Entscheidungen in Krisenmomenten

### Gesundheit (-100 bis +100)
```
-100: Schwer krank, arbeitsunfähig
 -50: Chronische Beschwerden, eingeschränkt
 -25: Häufig krank
   0: Durchschnittlich
 +25: Robust
 +50: Sehr gesund
+100: Außergewöhnlich vital
```

**Beeinflusst:**
- Arbeitsfähigkeit
- Lebenserwartung
- Militärtauglichkeit
- Familienplanung
- Kosten (Arzt, Ausfall)

### Ansehen (-100 bis +100)
```
-100: Geächtet, ausgestoßen
 -50: Schlecht beleumundet
 -25: Unauffällig
   0: Normal
 +25: Respektiert
 +50: Angesehen
 +75: Führungspersönlichkeit
+100: Legende in der Gemeinschaft
```

**Beeinflusst:**
- Hilfe von anderen
- Berufschancen
- Heiratschancen
- Politischer Einfluss
- Schutz bei Verfolgung

### Solidarität (-100 bis +100)
```
-100: Isoliert, keine Bindungen
 -50: Einzelgänger
   0: Normale Kontakte
 +25: Teil einer Gemeinschaft
 +50: Aktiv in Vereinen/Gewerkschaft
 +75: Vertrauensperson
+100: Zentrale Figur im Netzwerk
```

**Beeinflusst:**
- Hilfe in Krisen
- Zugang zu Informationen
- Kollektive Aktionen
- Schutz bei Verfolgung
- Generationenübergabe

---

## Ereignis-Flags (Ja/Nein)

Diese Flags tracken wichtige Entscheidungen:

### Allgemein
- `HAT_GEWERKSCHAFT_BEITRITT` — Gewerkschaftsmitglied?
- `HAT_SPD_BEITRITT` — Parteimitglied?
- `HAT_SOZIALISTENGESETZ_ERLEBT` — Verfolgung erlebt?
- `HAT_EXIL_ERFAHRUNG` — Im Exil gewesen?
- `HAT_GEFAENGNIS_ERFAHRUNG` — Im Gefängnis gewesen?
- `HAT_STREIK_TEILNAHME` — An Streik teilgenommen?
- `HAT_MILITAERDIENST` — Militärdienst geleistet?
- `HAT_KRIEGSTEILNAHME` — Im Krieg gekämpft?

### Familie
- `IST_VERHEIRATET` — Verheiratet?
- `HAT_KINDER` — Kinder?
- `HAT_FAMILIENVERLUST` — Kind/Partner verloren?
- `HAT_LIEBESEHE` — Aus Liebe geheiratet (vs. Vernunft)?

### Beruf
- `HAT_BERUF_GEWECHSELT` — Branche gewechselt?
- `HAT_AUFSTIEG` — Beruflicher Aufstieg?
- `HAT_ABSTIEG` — Beruflicher Abstieg?
- `IST_SELBSTSTAENDIG` — Eigenes Geschäft?

### Weltanschauung
- `HAT_RELIGION_VERLASSEN` — Kirche verlassen?
- `HAT_KONVERTIERT` — Religion gewechselt?
- `HAT_ATHEISMUS` — Atheist geworden?
- `HAT_NATIONALISMUS` — Nationalistisch?
- `HAT_INTERNATIONALISMUS` — Internationalistisch?

---

## Generationen-Vererbung

Bei Generationenwechsel:

### Direkte Vererbung (50%)
```
Kind.Bildung = (Eltern.Bildung * 0.5) + eigene_Entscheidungen
Kind.Vermögen = (Eltern.Vermögen * 0.5) + eigene_Entscheidungen
```

### Narrative Vererbung
Bestimmte Flags setzen Story-Bedingungen:

```
WENN Vater.HAT_SOZIALISTENGESETZ_ERLEBT = JA:
  → Sohn hat Zugang zu Geschichten über Untergrundkampf
  → Sohn.Politik-Basis +10 oder -10 (je nach Reaktion)

WENN Großvater.HAT_GEFAENGNIS_ERFAHRUNG = JA:
  → Enkelin kann davon erfahren
  → Entscheidungsmoment: Stolz oder Scham?
```

### Beispiel-Ketten

**Aufstiegskette:**
```
Gen1: Landarbeiter → Fabrikarbeiter (Vermögen +10)
Gen2: Fabrikarbeiter → Vorarbeiter (Vermögen +15, Ansehen +10)
Gen3: Kann Handwerkerlehre machen (Bildung +20)
Gen4: Kann Angestellter werden oder Meister
```

**Abstiegskette:**
```
Gen1: Handwerker → Arbeitslos nach Gründerkrach (Vermögen -30)
Gen2: Startet mit Vermögen -15, muss früh arbeiten
Gen3: Keine Bildungschance, bleibt ungelernt
Gen4: Armut verfestigt sich
```

**Politisierungskette:**
```
Gen1: Besucht SPD-Versammlung (Politik +15)
Gen2: Wächst in politischem Haushalt auf (Politik +10 Basis)
Gen3: Erlebt Repression → Radikalisierung (Politik +25)
Gen4: Bei Revolution 1918/19 → Schlüsselrolle möglich
```

---

## Schwellenwerte

### Kritische Schwellen

| Variable | Schwelle | Auswirkung |
|----------|----------|------------|
| Vermögen | < -50 | Armenhaus droht |
| Vermögen | > +50 | Kann Eigentum kaufen |
| Gesundheit | < -50 | Arbeitsunfähig |
| Gesundheit | < -75 | Lebensgefahr |
| Politik | > +50 | Gefährdet bei Repression |
| Politik | < -50 | Könnte Streikbrecher werden |
| Bildung | > +25 | Kann Zeitungen verstehen |
| Bildung | > +50 | Kann selbst schreiben |
| Ansehen | < -50 | Wird gemieden |
| Ansehen | > +50 | Kann andere überzeugen |

### Kombinationen

```
WENN Bildung > +25 UND Politik > 0:
  → Kann politische Literatur lesen
  → Zugang zu tieferen Entscheidungen

WENN Vermögen < -25 UND Gesundheit < 0:
  → Abwärtsspirale droht
  → Braucht Hilfe von außen (Solidarität wichtig)

WENN Ansehen > +50 UND Politik > +50:
  → Kann Führungsrolle übernehmen
  → Aber: Größeres Risiko bei Verfolgung
```

---

## Speichern des Spielstands

Für jede Generation wird gespeichert:

```yaml
familie: schumann
generation: 1
jahr: 1878
protagonist:
  name: "Wilhelm Schumann"
  alter: 28
  beruf: "Fabrikarbeiter"
  
attribute:
  bildung: 15
  vermoegen: -10
  politik: 35
  gesundheit: 10
  ansehen: 20
  solidaritaet: 40

flags:
  - HAT_GEWERKSCHAFT_BEITRITT
  - HAT_SPD_BEITRITT
  
narrative:
  - "Hat 1875 den Bildungsverein besucht"
  - "Hat 1877 Anna geheiratet (Liebesehe)"
  - "Hat 1878 verbotene Zeitungen versteckt"
```
