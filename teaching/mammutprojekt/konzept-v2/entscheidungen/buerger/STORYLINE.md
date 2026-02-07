# Familie Hoffmann — Bürger-Storyline

## Gesamtübersicht

```mermaid
graph TD
    subgraph "Generation 1: 1871-1890 — Die Gründerzeit"
        A[1871: Start als Kaufmannstochter] --> B{1873: Gründerkrach}
        B -->|Familie verarmt| C[Muss arbeiten: Lehrerin/Erzieherin]
        B -->|Familie übersteht| D[Normale Heiratsperspektive]
        C --> E{1876: Heirat trotz Beruf?}
        D --> E
        E -->|Liebesheirat| F[Weniger Geld, mehr Glück?]
        E -->|Vernunftehe| G[Sicherheit, aber Distanz]
        E -->|Ledig bleiben| H[Beruf + Stigma "alte Jungfer"]
        F --> I{1880: Kinder}
        G --> I
        H --> J[Frauenbewegung?]
        I --> K{1888: Töchter erziehen}
        J --> K
        K --> L[1890: Generation 1 endet]
    end
    
    subgraph "Generation 2: 1890-1914"
        L --> M[Tochter übernimmt]
        M --> N{1900: Studium möglich?}
        N -->|Ja| O[Neue Wege]
        N -->|Nein| P[Alte Muster]
    end
```

## Biografische Grundlagen

| Biografie | Elemente für Hoffmann-Familie |
|-----------|-------------------------------|
| **Hedwig Heyl** | Mustergültige Bürgerin, Fabrikanten-Gattin, Sozialreform |
| **Emilie Bücher** | Professorengattin, Umzüge, Briefe |
| **Anna Pappritz** | Was passiert ohne Heirat (Unfall) |
| **Hedwig Dohm** | Radikale Option, Schriftstellerin |
| **Franziska Tiburtius** | Ausbrechen: Ärztin werden |

## Start-Konfiguration (1871)

```yaml
protagonist:
  name: "Charlotte Hoffmann"
  geburtsjahr: 1855
  alter_1871: 16
  herkunft: "Leipzig, Kaufmannstochter"
  
attribute:
  bildung: 20       # Höhere Töchterschule
  vermoegen: 30     # Gutbürgerlich
  politik: -10      # Konservativ-unpolitisch
  gesundheit: 15    # Wohlgenährt
  ansehen: 25       # Gute Familie
  solidaritaet: 5   # Standesbewusst

flags: []
```

---

## Kapitel 1: 1871-1876 — Jugend und Weichenstellung

### [1871-Q1] Die höhere Tochter
**Kontext:** Charlotte ist 16, besucht die höhere Töchterschule in Leipzig. Die Reichsgründung ist fernes Echo.

> *"Wir wussten so gut wie nichts. Nicht weil wir dumm waren, sondern weil man uns dumm machte."*
> — Hedwig Dohm

**Szene:**
*Der Unterricht ist langweilig. Französisch, Handarbeit, ein bisschen Musik. Charlotte blättert heimlich in einem Buch, das sie im Arbeitszimmer des Vaters gefunden hat — Schiller.*

*Die Lehrerin bemerkt es. "Fräulein Hoffmann! Das ist keine passende Lektüre für ein junges Mädchen!"*

**Keine Entscheidung** — Einführung in die Welt der eingeschränkten Möglichkeiten.

---

### [1872-Q3] Das Pensionat
**Kontext:** Mit 17 soll Charlotte in ein Pensionat — der letzte Schliff vor der Ehe.

> *"Das Fräulein saß mit strenger Miene auf dem Sofa"*
> — Tiburtius über Gouvernanten

**Optionen:**

1. **Gehorsam ins Pensionat**
   - → Standard-Weg
   - → Ansehen +5
   - → Bildung +5 (Französisch, Musik, Konversation)
   - → Kontakte für spätere Heirat

2. **Widersprechen ("Ich will mehr lernen!")**
   - → Konflikt mit Eltern
   - → Bildung +0 (wird abgelehnt)
   - → Aber: Samen für später gepflanzt
   - → Vater evtl. beeindruckt (10% Chance: Privatunterricht)

3. **Krank werden (psychosomatisch)**
   - → Bleibt zu Hause
   - → Gesundheit -5
   - → Verzögerung, aber auch Freiheit zum Lesen

---

### [1873-Q2] Der Gründerkrach
**Kontext:** Die Familie Hoffmann hat in Eisenbahnaktien investiert. Der Crash trifft sie.

> *"Von einem Tag auf den anderen war alles anders."*

**Szene:**
*Der Vater kommt bleich nach Hause. Die Mutter weint. Charlotte versteht nicht alles, aber sie spürt: Etwas Schlimmes ist passiert.*

*"Die Aktien sind nichts mehr wert", sagt der Vater. "Wir müssen... uns einschränken."*

**Würfelwurf basierend auf Vermögen:**

- **Vermögen > 30:** Familie übersteht mit Verlusten
  - → Vermögen -20
  - → Weiter wie geplant
  
- **Vermögen 10-30:** Schwere Einschnitte
  - → Vermögen -30
  - → Dienstmädchen entlassen
  - → Charlotte muss im Haushalt helfen
  - → Heiratschancen sinken (Ansehen -10)
  
- **Vermögen < 10:** Ruin
  - → Vermögen auf -30
  - → Charlotte MUSS arbeiten
  - → Weg zur Lehrerin/Erzieherin

---

### [1874-Q2] Der Ball (wenn nicht ruiniert)
**Kontext:** Charlotte ist 19, auf ihrem ersten Ball. Zeit, einen Mann zu finden.

> *"Ein Schiff, das zur Abfahrt im Hafen liegt und auf den Windstoß wartet"*
> — Tiburtius

**Szene:**
*Der Ballsaal glitzert. Charlotte trägt ihr bestes Kleid — das einzige, das noch passt nach den Sparmaßnahmen. Ihre Mutter beobachtet jeden ihrer Schritte.*

*Ein junger Mann bittet sie zum Tanz. Er ist Jurist, aus guter Familie. Höflich, aber langweilig.*

*Später, in einer Ecke, steht ein anderer. Weniger elegant, aber seine Augen funkeln. Er spricht über Bücher. Über Ideen.*

**Optionen:**

1. **Den Juristen ermutigen (Vernunft)**
   - → Sichere Partie
   - → Führt zu Vernunftehe
   - → Vermögen +15 (seine Familie)
   - → Ansehen +10

2. **Den Idealisten suchen (Herz)**
   - → Riskanter
   - → Könnte Liebesheirat werden
   - → Vermögen +0 oder sogar -5
   - → Aber: Bildung +10 (er teilt Bücher)

3. **Keinen ermutigen ("Ich will noch warten")**
   - → Mutter enttäuscht
   - → Mehr Zeit, aber Druck steigt
   - → Nächstes Jahr: Optionen weniger

---

### [1875-Q1] Die Wahl (wenn Lehrerin-Pfad)
**Kontext:** Nach dem Ruin muss Charlotte arbeiten. Aber wie?

> *"Dem weiblichen Wesen gemäße Berufsbilder als Zwischenlösung"*
> — Schraut über "erlaubte" Frauenberufe

**Optionen:**

1. **Lehrerinnenseminar**
   - → 2 Jahre Ausbildung
   - → Vermögen -10 (Kosten)
   - → Bildung +20
   - → Beruf: Lehrerin an Mädchenschule
   - → Ansehen +5 (respektabel)

2. **Erzieherin in "guten Häusern"**
   - → Sofort Einkommen
   - → Vermögen +5
   - → Ansehen -5 (Dienstboten-nah)
   - → Aber: Kontakte zu höheren Kreisen

3. **Haushälterin beim Bruder/Onkel**
   - → Kein Stigma
   - → Vermögen +0
   - → Aber: Abhängig, keine Zukunft

---

### [1876-Q3] Die Entscheidung: Heirat
**Kontext:** Charlotte ist 21. Ein Antrag liegt vor (je nach früherem Pfad unterschiedlich).

**Szene (Vernunft-Pfad):**
*Der Jurist — Heinrich heißt er — hat um ihre Hand angehalten. Er ist solide, hat Aussichten, und die Familie ist einverstanden.*

*Charlotte steht am Fenster. Draußen regnet es. Sie denkt an die Bücher, die sie nie lesen wird. An die Gespräche, die sie nie führen wird.*

*Ihre Mutter kommt herein. "Nun? Was sagst du ihm?"*

**Optionen:**

1. **Ja sagen**
   - → Flag: VERHEIRATET
   - → Flag: VERNUNFTEHE
   - → Vermögen +20
   - → Ansehen +15
   - → Freiheit -30 (unsichtbare Variable)
   - → Neuer Lebensabschnitt

2. **Um Bedenkzeit bitten**
   - → Mutter entsetzt
   - → Ansehen -5
   - → Aber: Mehr Optionen prüfen

3. **Nein sagen**
   - → Skandal in der Familie!
   - → Ansehen -20
   - → Aber: Flag: UNABHÄNGIG
   - → Muss anderen Weg finden

---

## Kapitel 2: 1877-1885 — Die junge Ehefrau/Berufstätige

### [1877-Q2] Das erste Jahr (wenn VERHEIRATET)
**Kontext:** Charlotte ist jetzt Frau eines aufstrebenden Juristen/Kaufmanns.

> *"Ehelicher Alltag – die Gattin an seiner Seite"*
> — Schraut

**Szene:**
*Das neue Haus. Die neuen Pflichten. Das neue Dienstmädchen, das Charlotte nicht weiß wie anzuleiten.*

*Ihr Mann kommt spät nach Hause. Er erzählt von seiner Arbeit. Charlotte hört zu, aber sie versteht wenig — man hat ihr ja nie etwas beigebracht.*

*Manchmal, wenn er schläft, liest sie heimlich.*

**Keine Entscheidung** — Stimmungsbild

---

### [1878-Q1] Das Dienstmädchen
**Kontext:** Das Dienstmädchen Marie ist krank. Was tun?

> *"Das Kreuz mit den Dienstboten"*
> — Schraut

**Szene:**
*Marie hustet seit Tagen. Sie sagt, es sei nichts, aber Charlotte sieht: Das Mädchen ist krank.*

*Die Nachbarin rät: "Entlassen Sie sie. Bevor sie die ganze Familie ansteckt. Es gibt genug andere."*

*Aber Marie hat keine Familie. Wohin soll sie?*

**Optionen:**

1. **Marie entlassen (Standard)**
   - → Ansehen +5 (bei Nachbarinnen)
   - → Vermögen +5 (keine Lohnfortzahlung)
   - → Aber: Schuldgefühle
   - → Marie verschwindet aus der Geschichte

2. **Marie behalten und pflegen**
   - → Vermögen -10 (Arzt, Zeit)
   - → Ansehen -5 ("zu weich")
   - → Aber: Solidarität +15
   - → Marie wird loyal (hilft später)
   - → Gesundheitsrisiko (10% krank werden)

3. **Marie zu ihren Eltern schicken (Kompromiss)**
   - → Vermögen -5 (Reisekosten)
   - → Neutral
   - → Marie kommt vielleicht zurück

---

### [1880-Q2] Das Kind
**Kontext:** Charlotte bekommt ihr erstes Kind.

> *"Mutterschaft"*
> — Schraut

**Szene:**
*Eine Tochter. Emma. Klein, verletzlich, wunderbar.*

*Die Mutter sagt: "Ein Mädchen. Naja. Vielleicht das nächste Mal ein Junge."*

*Charlotte schaut auf das Kind in ihren Armen und denkt: Sie soll es besser haben als ich.*

**Keine Entscheidung** — Aber: Generation 2 beginnt

→ Flag: HAT_KINDER
→ Kind: Emma Hoffmann, geb. 1880

---

### [1882-Q3] Die Töchter-Erziehung
**Kontext:** Emma ist 2. Charlotte denkt an die Zukunft.

> *"Vorbereitung auf die künftige Frauenrolle"*
> — Schraut

**Szene:**
*Charlotte beobachtet Emma beim Spielen. Das Mädchen ist neugierig, stellt Fragen, will alles wissen.*

*"Genau wie ich war", denkt Charlotte. "Und man hat mich klein gehalten."*

*Ihr Mann kommt: "Ich habe mich nach einer Gouvernante erkundigt. Für später."*

**Optionen (wirkt auf Generation 2!):**

1. **Traditionelle Erziehung**
   - → Emma: Bildung Basis = 10
   - → Emma: Ansehen Basis = 20
   - → Reproduktion des Systems

2. **Bessere Bildung fordern**
   - → Konflikt mit Mann (leicht)
   - → Emma: Bildung Basis = 25
   - → Emma: Hat mehr Optionen später

3. **Heimlich fördern**
   - → Charlotte liest Emma vor, lehrt sie selbst
   - → Emma: Bildung Basis = 20
   - → Besondere Bindung Mutter-Tochter

---

### [1885-Q2] Die Frauenbewegung
**Kontext:** Charlotte hört von der Frauenbewegung. Vereine entstehen.

> *"Die bürgerliche Frauenbewegung"*
> — Schraut

**Szene:**
*Eine Bekannte erzählt von einem Vortrag. "Über Frauenbildung. Stell dir vor — manche fordern, dass Frauen studieren dürfen!"*

*Charlotte horcht auf. Studieren?*

*"Natürlich absurd", fährt die Bekannte fort. "Aber unterhaltsam."*

**Optionen:**

1. **Desinteresse ("Das ist nichts für mich")**
   - → Alles bleibt
   - → Konservatives Weltbild bleibt

2. **Heimliches Interesse**
   - → Besorgt sich Flugblätter
   - → Politik +10
   - → Bildung +5
   - → Vorsichtig

3. **Offen hingehen**
   - → Ansehen -10 (in konservativen Kreisen)
   - → Ansehen +10 (in progressiven Kreisen)
   - → Politik +15
   - → Neue Kontakte

---

## Kapitel 3: 1886-1890 — Reife Jahre

### [1888-Q1] Der Tod des Kaisers
**Kontext:** Wilhelm I. stirbt. Friedrich III. stirbt nach 99 Tagen. Wilhelm II. kommt.

> *"Das Dreikaiserjahr"*

**Szene:**
*Alle reden von der Hoffnung auf Friedrich — den liberalen Kaiser. Und dann ist er tot.*

*Charlottes Mann: "Wilhelm II. wird anders. Jünger, dynamischer."*

*Charlotte denkt: Dynamisch. Aber in welche Richtung?*

**Keine Entscheidung** — Stimmungsbild, historischer Kontext

---

### [1890-Q1] Die Tochter wird zehn
**Kontext:** Emma ist 10. Die wichtigen Jahre beginnen.

**Szene:**
*Emma kommt aus der Schule. Sie hat Fragen. Über alles.*

*"Mama, warum darf ich nicht aufs Gymnasium wie Paul von nebenan?"*

*Charlotte weiß keine gute Antwort.*

**Markiert ENDE GENERATION 1**

---

## Übergang zu Generation 2

### Emma übernimmt

**Basis-Werte (aus Generation 1):**
```
Emmas Bildung = (Mutter Bildung × 0.5) + Kindheitserfahrungen
Emmas Politik = (Mutter Politik × 0.5) + Kindheitserfahrungen
```

**Neue Möglichkeiten (1890-1914):**
- Höhere Mädchenschulreform
- Erstes Frauenstudium (ab 1900 in Baden!)
- Neue Berufe öffnen sich
- Aber: Gesellschaftliche Widerstände bleiben

---

## Konsequenzen-Ketten (Bürger)

### Bildung → Studierende Tochter?
```
1872: Charlotte will mehr lernen
      ↓
1882: Charlotte fördert Emma heimlich
      ↓
1895: Emma will Lehrerin werden
      ↓
1900: Emma will studieren!
      ↓
1905: Emma wird Ärztin? (wie Tiburtius)
```

### Verarmung → Klassenwechsel
```
1873: Familie ruiniert
      ↓
1876: Charlotte wird Erzieherin
      ↓
1885: Charlotte trifft SPD-Frauen
      ↓
1890: Charlotte wie Lily Braun?
      ↓
Kind: Wächst zwischen den Klassen auf
```

### Dienstmädchen → Solidarität
```
1878: Marie gepflegt statt entlassen
      ↓
1890: Marie immer noch da, loyal
      ↓
1900: Marie erzählt von Arbeiterleben
      ↓
Emma: Versteht beide Seiten
      ↓
1918: Kann zwischen Klassen vermitteln
```
