# METHODEN_HISTORIE Template

**Version:** 4.0 (24.01.2025)
**Zweck:** Tracking vergangener Methoden für Variationsformel
**Speicherort:** Project Knowledge (pro Fach-Projekt)

---

## Verwendung

Diese Datei wird im **Project Knowledge** gespeichert und bei jeder Unterrichtsplanung:
1. **Gelesen** (am Anfang der Planung)
2. **Aktualisiert** (am Ende der Planung via `methoden-historie-update.md`)

---

## Variationsformel

| Verwendungen in Folge | Status | Aktion |
|----------------------|--------|--------|
| 1x | ✅ OK | Frei verwendbar |
| 2x | ⚠️ Warnung | Alternative vorschlagen |
| 3x | 🔴 Gesperrt | NICHT verwenden, Alternative PFLICHT |

**Referenz für Alternativen:** `/mnt/skills/user/methoden-bibliothek/SKILL.md`

---

# Template (Copy-Paste in Project Knowledge)

```markdown
# Methoden-Historie: {{PROJEKT_NAME}}

**Fach:** {{FACH}}
**Klasse:** {{KLASSE}}
**Erstellt:** {{DATUM}}
**Letzte Aktualisierung:** {{DATUM}}

---

## Letzte Verwendungen

| Datum | Stunde/Thema | Einstieg | Erarbeitung | Sicherung |
|-------|--------------|----------|-------------|-----------|
| {{DATUM}} | {{THEMA}} | {{METHODE}} | {{METHODE}} | {{METHODE}} |
| {{DATUM}} | {{THEMA}} | {{METHODE}} | {{METHODE}} | {{METHODE}} |
| {{DATUM}} | {{THEMA}} | {{METHODE}} | {{METHODE}} | {{METHODE}} |
| {{DATUM}} | {{THEMA}} | {{METHODE}} | {{METHODE}} | {{METHODE}} |
| {{DATUM}} | {{THEMA}} | {{METHODE}} | {{METHODE}} | {{METHODE}} |

---

## Variationswarnungen

### ⚠️ Warnung (2x in letzten 3 Stunden)
- {{METHODE}} → Alternative wählen empfohlen

### 🔴 Gesperrt (3x in letzten 3 Stunden)
- {{METHODE}} → NICHT mehr verwenden!

---

## Methoden-Statistik

### Einstieg
| Methode | Verwendungen | Letzte Nutzung |
|---------|--------------|----------------|
| Bildimpuls | {{ANZAHL}} | {{DATUM}} |
| Brainstorming | {{ANZAHL}} | {{DATUM}} |
| Blitzlicht | {{ANZAHL}} | {{DATUM}} |

### Erarbeitung
| Methode | Verwendungen | Letzte Nutzung |
|---------|--------------|----------------|
| Gruppenarbeit | {{ANZAHL}} | {{DATUM}} |
| Think-Pair-Share | {{ANZAHL}} | {{DATUM}} |
| Einzelarbeit | {{ANZAHL}} | {{DATUM}} |

### Sicherung
| Methode | Verwendungen | Letzte Nutzung |
|---------|--------------|----------------|
| Blitzlicht | {{ANZAHL}} | {{DATUM}} |
| Präsentation | {{ANZAHL}} | {{DATUM}} |
| Exit Ticket | {{ANZAHL}} | {{DATUM}} |

---

## Anleitung

### Bei Planungsstart:
1. Diese Datei lesen
2. Gesperrte Methoden notieren
3. Warnungen beachten

### Bei Methodenwahl:
- Gesperrte Methode → Alternative aus methoden-bibliothek wählen
- Warnung → Alternative vorschlagen, User entscheidet

### Nach Planung:
1. `methoden-historie-update.md` von Chat erhalten
2. Neue Zeilen in "Letzte Verwendungen" einfügen
3. Variationswarnungen neu berechnen
4. Diese Datei in Project Knowledge aktualisieren

---

*Stand: {{TIMESTAMP}}*
```

---

# Update-Template (von Chat erstellt)

```markdown
# Methoden-Historie Update

**Projekt:** {{PROJEKT_ID}}
**Datum:** {{DATUM}}

---

## Neue Einträge

Bitte in die methoden-historie.md einfügen (ganz oben in der Tabelle):

| Datum | Stunde/Thema | Einstieg | Erarbeitung | Sicherung |
|-------|--------------|----------|-------------|-----------|
| {{DATUM}} | {{THEMA_1}} | {{METHODE_E1}} | {{METHODE_ER1}} | {{METHODE_S1}} |
| {{DATUM}} | {{THEMA_2}} | {{METHODE_E2}} | {{METHODE_ER2}} | {{METHODE_S2}} |

---

## Variationswarnungen (aktualisiert)

Nach dem Update:

### ⚠️ Warnung
- {{METHODE}} (jetzt {{ANZAHL}}x)

### 🔴 Gesperrt  
- {{METHODE}} (jetzt {{ANZAHL}}x)

---

## Anweisung

1. Öffne deine `methoden-historie.md` im Project Knowledge
2. Füge die neuen Einträge oben in die Tabelle ein
3. Aktualisiere den Abschnitt "Variationswarnungen"
4. Speichere die Datei

---

*Update erstellt: {{TIMESTAMP}}*
```

---

## Beispiel: Ausgefüllte Historie

```markdown
# Methoden-Historie: AV3_LWK_BPE1

**Fach:** Lebensweltkompetenz (LWK)
**Klasse:** AV3
**Erstellt:** 15.01.2025
**Letzte Aktualisierung:** 24.01.2025

---

## Letzte Verwendungen

| Datum | Stunde/Thema | Einstieg | Erarbeitung | Sicherung |
|-------|--------------|----------|-------------|-----------|
| 24.01 | Bewerbungsgespräch | Video-Stopp | Rollenspiel | Exit Ticket |
| 22.01 | Anschreiben | Bildimpuls | Textanalyse | Blitzlicht |
| 20.01 | Lebenslauf | Bildimpuls | Einzelarbeit | Blitzlicht |
| 17.01 | Stärkenanalyse | Brainstorming | Gruppenarbeit | Präsentation |
| 15.01 | Berufsfelder | Murmelphase | Gallery Walk | Blitzlicht |

---

## Variationswarnungen

### ⚠️ Warnung (2x in letzten 3 Stunden)
- **Bildimpuls** → Alternative: Zitat-Reaktion, Video-Stopp, Concept Cartoon

### 🔴 Gesperrt (3x in letzten 3 Stunden)
- **Blitzlicht** → NICHT mehr verwenden! Alternativen: Exit Ticket, One-Minute-Paper, 3-2-1

---

## Methoden-Statistik

### Einstieg
| Methode | Verwendungen | Letzte Nutzung |
|---------|--------------|----------------|
| Bildimpuls | 2 | 22.01 |
| Brainstorming | 1 | 17.01 |
| Video-Stopp | 1 | 24.01 |
| Murmelphase | 1 | 15.01 |

### Erarbeitung
| Methode | Verwendungen | Letzte Nutzung |
|---------|--------------|----------------|
| Einzelarbeit | 1 | 20.01 |
| Gruppenarbeit | 1 | 17.01 |
| Gallery Walk | 1 | 15.01 |
| Rollenspiel | 1 | 24.01 |
| Textanalyse | 1 | 22.01 |

### Sicherung
| Methode | Verwendungen | Letzte Nutzung |
|---------|--------------|----------------|
| Blitzlicht | 3 | 22.01 |
| Präsentation | 1 | 17.01 |
| Exit Ticket | 1 | 24.01 |

---

*Stand: 24.01.2025, 14:30*
```

---

## Schnellreferenz: Alternativen

Aus `/mnt/skills/user/methoden-bibliothek/SKILL.md`:

### Einstieg-Alternativen
| Gesperrt | Alternativen |
|----------|--------------|
| Bildimpuls | Zitat-Reaktion, Concept Cartoon, Video-Stopp |
| Brainstorming | Murmelphase, Stummes Schreibgespräch |
| Blitzlicht | Positionslinie, Vier-Ecken-Methode |

### Erarbeitungs-Alternativen
| Gesperrt | Alternativen |
|----------|--------------|
| Gruppenarbeit | Placemat, Lerntempoduett, World Café |
| Einzelarbeit | Reziprokes Lesen, Lerntempoduett |
| Gallery Walk | Marktplatz der Ideen, Museumsgang |

### Sicherungs-Alternativen
| Gesperrt | Alternativen |
|----------|--------------|
| Blitzlicht | Murmelgruppe, One-Minute-Paper |
| Exit Ticket | 3-2-1 Methode, Fünf-Finger-Feedback |
| Präsentation | Elevator Pitch, Fishbowl |

---

## Version History

| Version | Datum | Änderungen |
|---------|-------|------------|
| **4.0** | **24.01.2025** | **Initiale Erstellung für Methoden-Tracking** |
