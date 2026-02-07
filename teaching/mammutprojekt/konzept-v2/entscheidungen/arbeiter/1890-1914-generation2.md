# Generation 2: Karl Schumann (1890-1914)

## Übergang von Generation 1

### Start-Situation
```yaml
protagonist:
  name: "Karl Schumann"
  geburtsjahr: 1880
  alter_1890: 10
  vater: "August Schumann"
  
erbe_von_vater:
  bildung: [FORMEL: (Vater × 0.5) + Kindheit]
  vermoegen: [FORMEL: (Vater × 0.5)]
  politik: [FORMEL: (Vater × 0.5) + Kindheitserfahrungen]
  
narrative_aus_gen1:
  - [variabel je nach Vater-Entscheidungen]
```

### Beispiel-Startprofile

**Wenn Vater im Untergrund war:**
```yaml
basis:
  bildung: 20      # Vater hat Bildung gefördert
  politik: 25      # "Mein Vater wurde verfolgt"
  
narrative:
  - "Dein Vater hat unter dem Sozialistengesetz gekämpft"
  - "Du erinnerst dich an die Nacht, als die Polizei kam"
```

**Wenn Vater ausgestiegen ist:**
```yaml
basis:
  bildung: 15
  politik: -5      # Distanz zur Bewegung
  
narrative:
  - "Dein Vater zog sich zurück"
  - "Die alten Genossen grüßen nicht mehr"
```

---

## Kapitel 1: 1890-1900 — Die neuen Zeiten

### [1890-Q4] Die SPD ist wieder legal
**Kontext:** Karl ist 10. Die Erwachsenen feiern. Die SPD ist zurück.

**Szene:**
*Überall rote Fahnen. Dein Vater weint. Du verstehst nicht alles, aber du spürst: Etwas Wichtiges ist passiert.*

*"Jetzt können wir offen kämpfen", sagt er.*

**Kindheitsprägung:**
- Dieses Ereignis formt Karls politische Identität
- Wenn Vater im Untergrund: Karl erlebt den Triumph
- Wenn Vater ausgestiegen: Karl erlebt den Ausschluss

---

### [1893-Q2] Die Lehre
**Kontext:** Karl ist 13. Was wird er?

> *Generation 1 hat Weichen gestellt: Schulbildung bestimmt Optionen.*

**Szene:**
*Der Schulmeister spricht mit deinem Vater.*

*"Karl ist begabt. Er könnte mehr werden als ein Fabrikarbeiter."*

*Dein Vater denkt an seine eigene Jugend. An die Bücher, die er erst spät entdeckte.*

**Optionen (abhängig von Karls Bildung):**

**Wenn Bildung > 20:**
1. **Handwerkerlehre (Schlosser, Drucker)**
   - → Bildung +10
   - → Vermögen +5
   - → Qualifizierter Arbeiter
   - → Gewerkschafts-Potenzial

2. **Kaufmannslehre**
   - → Bildung +15
   - → Ansehen +10
   - → Aufstieg möglich
   - → Aber: Entfernung von der Klasse?

3. **Weiter Schule (Realschule)**
   - → Bildung +20
   - → Vermögen -10 (Kosten)
   - → Noch mehr Optionen später

**Wenn Bildung < 15:**
1. **Fabrikarbeit (ungelernt)**
   - → Wie der Vater
   - → Vermögen +5
   - → Reproduktion der Klassenlage

2. **Hilfsarbeiter**
   - → Minimal
   - → Harte Arbeit, wenig Perspektive

---

### [1895-Q1] Die erste Liebe
**Kontext:** Karl ist 15. Er lernt ein Mädchen kennen.

**Szene:**
*Anna arbeitet in der Weberei. Sie ist ein Jahr älter, mit schnellen Augen und einem Lachen, das dich verfolgt.*

*Ihr Vater ist Gewerkschafter. Dein Vater kennt ihn aus dem Bildungsverein — oder auch nicht, je nach seiner Geschichte.*

**Optionen:**

1. **Werben (traditionell)**
   - → Solide Beziehung
   - → Vermögen -5 (Geschenke, Ausgehen)
   - → Frühe Bindung

2. **Freundschaft erstmal**
   - → Langsamer, aber tiefere Beziehung
   - → Sie wird Genossin? Oder kritisch?

3. **Nicht interessiert (Arbeit/Politik wichtiger)**
   - → Bleibt ungebunden
   - → Mehr Zeit für anderes

---

### [1898-Q3] Die Gewerkschaft
**Kontext:** Karl ist 18. Die freien Gewerkschaften wachsen.

> *Nach dem Sozialistengesetz: legale Massenorganisation.*

**Szene:**
*In der Fabrik spricht man von der Gewerkschaft. Sie fordern bessere Löhne, kürzere Arbeitszeiten.*

*Dein Vorarbeiter sagt: "Halt dich da raus. Das macht nur Ärger."*

*Aber dein Kollege Friedrich sagt: "Ohne uns hätten sie nichts. Zeit, dass sie das merken."*

**Optionen:**

1. **Beitreten**
   - → Flag: GEWERKSCHAFTSMITGLIED
   - → Solidarität +20
   - → Politik +10
   - → Netzwerk in der Bewegung

2. **Sympathisieren, aber nicht beitreten**
   - → Vorsichtig
   - → Bei Streiks: Entscheidung neu

3. **Ablehnen**
   - → Ruhe
   - → Aber: Isolation von Kollegen

---

### [1900-Q1] Die Jahrhundertwende
**Kontext:** Neues Jahrhundert. Deutschland ist Weltmacht. Die SPD wächst.

**Szene:**
*Alle reden vom neuen Jahrhundert. Was wird es bringen?*

*Dein Vater sagt: "Die SPD wird siegen. Es ist nur eine Frage der Zeit."*

*Aber andere sagen: "Der Kaiser hat Flotten. Er hat Kolonien. Er will Krieg."*

**Stimmungsbild — keine Entscheidung**

---

## Kapitel 2: 1900-1910 — Die Massenpartei

### [1903-Q2] Die Reichstagswahl
**Kontext:** SPD wird stärkste Partei bei Stimmen (31,7%).

**Szene:**
*Die Nachricht geht durch die Fabrik wie ein Lauffeuer. Ein Drittel aller Deutschen hat SPD gewählt!*

*"Wir sind die Mehrheit", sagt Friedrich. "Bald müssen sie uns regieren lassen."*

*Aber: Im Reichstag haben sie weniger Sitze, weil die Wahlkreise ungerecht sind.*

**Entscheidung:**

1. **Optimismus ("Der Sieg ist nahe!")**
   - → Politik +10
   - → Engagement +10
   - → Reformistisch

2. **Kritik ("Wahlen reichen nicht")**
   - → Politik +15
   - → Radikalisierung
   - → "Generalstreik statt Wahlzettel!"

3. **Desinteresse ("Politik ändert nichts")**
   - → Politik -10
   - → Konzentration auf Privatleben

---

### [1905-Q1] Revolution in Russland
**Kontext:** In Russland bricht Revolution aus. Arbeiter gegen den Zaren.

**Szene:**
*Die Zeitungen berichten: Arbeiterräte in Petersburg! Der Zar schwankt!*

*In der SPD debattieren sie: Sollen wir auch streiken? Die "Massenstreik-Debatte".*

*Rosa Luxemburg sagt: Ja! Der Parteivorstand sagt: Zu gefährlich.*

**Optionen:**

1. **Für Massenstreik (radikal)**
   - → Politik +20
   - → Solidarität +10
   - → Konflikt mit Parteiführung

2. **Gegen Massenstreik (reformistisch)**
   - → Politik +5
   - → Ansehen +5 bei Parteiführung
   - → Aber: Revolutionäre enttäuscht

3. **Unentschieden**
   - → Intern zerrissen

---

### [1906-Q2] Heirat
**Kontext:** Karl ist 26. Zeit für eine Familie.

**Szene (wenn Anna-Beziehung besteht):**
*Anna sitzt neben dir. Ihr seid jetzt zehn Jahre befreundet. Mehr als befreundet.*

*"Wir könnten heiraten", sagst du.*

*Sie lacht. "Endlich fragst du."*

**Optionen:**

1. **Heiraten**
   - → Flag: VERHEIRATET
   - → Anna bringt eigene Geschichte mit
   - → Vermögen -10 (Hochzeit, Wohnung)
   - → Generation 3 beginnt bald

2. **Noch warten**
   - → Flexibel bleiben
   - → Aber: Anna wartet nicht ewig

---

### [1908-Q3] Das erste Kind
**Kontext:** Ein Kind wird geboren.

**Szene:**
*Du hältst deinen Sohn. Wilhelm. Nach dem Kaiser? Nein — nach deinem Großvater.*

*Du denkst: Was wird aus ihm? In welcher Welt wird er aufwachsen?*

→ Flag: HAT_KINDER
→ Kind: Wilhelm Schumann, geb. 1908 (Generation 3)

---

## Kapitel 3: 1910-1914 — Vor dem Sturm

### [1912-Q1] Die große Wahl
**Kontext:** SPD erreicht 34,8% — stärkste Fraktion im Reichstag!

**Szene:**
*110 Abgeordnete! Mehr als jede andere Partei!*

*"Jetzt MÜSSEN sie uns an die Regierung lassen", sagt jemand.*

*Aber: Der Kaiser ignoriert den Reichstag. Der Kanzler wird nicht gewählt.*

**Stimmungsbild:**
- Triumph und Frustration
- So nah und doch so fern

---

### [1913-Q2] Die Zabern-Affäre
**Kontext:** Ein Leutnant beleidigt Elsässer, Militär schlägt Zivilisten. Der Reichstag protestiert — und wird ignoriert.

**Szene:**
*"Das Militär steht über dem Gesetz", sagt dein Vater. "Sie lachen über uns."*

*Du spürst: Etwas Dunkles kommt. Krieg? Revolution?*

---

### [1914-Q2] Die Julikrise
**Kontext:** Attentat in Sarajevo. Die Mächte mobilisieren.

**Szene:**
*Juni war noch normal. Juli ist Wahnsinn.*

*Jeden Tag neue Schlagzeilen: Österreich! Serbien! Russland! Frankreich!*

*Am 1. August erklärt Deutschland Russland den Krieg.*

---

### [1914-Q3] Der Burgfrieden — DIE ENTSCHEIDUNG
**Kontext:** Am 4. August stimmt die SPD für die Kriegskredite.

> *"Ich kenne keine Parteien mehr, ich kenne nur noch Deutsche!"*
> — Kaiser Wilhelm II.

**Szene:**
*Du stehst vor der Fabrik. Die Kollegen reden durcheinander.*

*"Die SPD hat für den Krieg gestimmt! Für den KRIEG!"*

*Einige jubeln: "Endlich Einheit! Wir verteidigen das Vaterland!"*

*Andere sind entsetzt: "Verrat! Sie haben die Internationale verraten!"*

*Du musst dich entscheiden.*

**DIE GROSSE ENTSCHEIDUNG:**

1. **Für den Burgfrieden ("Vaterlandsverteidiger")**
   - → Politik -20 (Rechtsruck)
   - → Ansehen +10 (patriotisch)
   - → Solidarität -10 (mit Internationalisten)
   - → Führt zu: Mehrheits-SPD, später SPD

2. **Gegen den Burgfrieden ("Internationalist")**
   - → Politik +30 (Radikalisierung)
   - → Ansehen -20 (als Vaterlandsverräter)
   - → Solidarität +20 (mit Radikalen)
   - → Führt zu: USPD, später KPD oder Linke SPD

3. **Zerrissen (innerlich gespalten)**
   - → Kein klares Bekenntnis
   - → Kann später beide Seiten verstehen
   - → Aber: Nirgends ganz dazugehören

---

## Übergang zu Generation 3

### Wilhelm übernimmt (1914: 6 Jahre alt)

**Der Erste Weltkrieg:**
- Wilhelm erlebt als Kind: Hunger, Entbehrung, Vaters Abwesenheit
- 1918: Revolution
- 1919: Weimarer Republik

**Generation 3: 1914-1933**
- Hyperinflation 1923
- Goldene Zwanziger
- Weltwirtschaftskrise 1929
- Aufstieg der NSDAP
- 1933: Machtergreifung

---

## Konsequenzketten Generation 2 → Generation 3

### Burgfrieden-Entscheidung → 1918/1933

**Wenn Burgfrieden (Vaterlandsverteidiger):**
```
1914: Für Krieg gestimmt
      ↓
1917: Bleibt bei SPD
      ↓
1918: Bei Ebert-Noske-Flügel
      ↓
1919: Unterstützt Weimar
      ↓
1933: SPD wird verboten — aber überlebt eher im Untergrund
```

**Wenn gegen Burgfrieden (Internationalist):**
```
1914: Gegen Krieg
      ↓
1917: USPD-Gründung
      ↓
1918: Bei Radikalen / Spartakus
      ↓
1919: KPD? Rosa Luxemburg ermordet!
      ↓
1933: Kommunist — gefährlichere Position
```

---

## Karl Schumanns Alternativen

### Pfad A: Der Gewerkschaftsführer
- Gewerkschaftsmitglied → Funktionär → Bezirksleiter
- Bei Burgfrieden: Bleibt bei Freien Gewerkschaften
- 1933: Wird verhaftet, Konzentrationslager?

### Pfad B: Der Parteifunktionär
- SPD-Mitglied → Ortsverein → Stadtrat
- Bei Burgfrieden: Mehrheits-SPD
- 1933: Emigration oder Verhaftung

### Pfad C: Der Radikale
- USPD/Spartakus → KPD
- 1919: Überlebt Januaraufstand?
- 1933: Erste Welle der Verhaftungen

### Pfad D: Der Unpolitische
- Nie Partei beigetreten
- Konzentration auf Familie
- 1933: "Wir haben ja nichts getan..." — überlebt?
