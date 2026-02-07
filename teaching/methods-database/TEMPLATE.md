# Paper → Notion Template

*Workflow: Paper-Link schicken → Aether erstellt beides automatisch*

---

## 1. Paper-Zusammenfassung (eigene Notion-Seite)

Wird als Unterseite von "Teaching Methods" angelegt.

### Struktur:

```
📄 [Callout] Vollständige Zitation + DOI

---

📌 These
   → Was behauptet das Paper? Zentrale Hypothese/Argument in 2-3 Sätzen.

🔬 Methode
   → Wie wurde geforscht? (Meta-Analyse, RCT, qualitativ...)
   → Stichprobe, Datenbanken, Analysemethode

💡 Erkenntnisse
   → Hauptergebnis (Effektstärke wenn vorhanden)
   → Wichtige Moderatoren/Unterbefunde
   → Überraschende Befunde

⚠️ Kritik & Limitationen
   → Methodische Schwächen
   → Inhaltliche Einschränkungen
   → Was fehlt?

🎓 Relevanz für die Unterrichtspraxis
   → Konkrete Handlungsempfehlungen
   → Was bedeutet das für den Unterricht?
   → Dos and Don'ts
```

---

## 2. Methoden-Datenbank-Eintrag (in Inline-DB)

### Felder:

| Feld | Typ | Beschreibung |
|------|-----|-------------|
| **Name** | Title | Methodenname (DE + EN) |
| **Kategorie** | Select | Activation, Cooperation, Reflection, Assessment, Differentiation, Digital |
| **Sozialform** | Multi-Select | Einzelarbeit, Partnerarbeit, Gruppenarbeit, Plenum |
| **Dauer** | Multi-Select | 5 min, 15 min, 45 min, 90 min, Projekt |
| **Effektstaerke** | Text | z.B. "g = .55 (CI: .45–.65)" |
| **Evidenz** | Select | Meta-Analyse, RCT, Erfahrungswissen |
| **Faecher** | Multi-Select | Alle, Politik, Englisch, Sozialpaedagogik, Lebensweltkunde |
| **Quelle** | Text | Kurzreferenz: "Autor (Jahr), Journal" |
| **Praxisrelevanz** | Text | 1-2 Sätze: Was heißt das konkret für meinen Unterricht? |

### Seiteninhalt des DB-Eintrags:

```
## Beschreibung
   → Was ist die Methode? 2-3 Sätze.

## Durchführung
   → Varianten mit Zeitangaben und Schritten

## Beispiel-Prompts / Beispiele
   → Konkret für Toms Fächer: Politik/Geschichte, Englisch, Sozialpädagogik

## ⚡ Tipps
   → Dos and Don'ts (bold)

## 📊 Evidenz
   → Effektstärke + Kontext
   → ⚠️ Callout mit Limitationen
```

---

## 3. Lokale Markdown-Spiegelung

Parallel werden erstellt:
- `methods-database/methods/{methode}.md` — Ausführliche Methodenkarte
- `methods-database/sources/{autor-jahr-thema}.md` — Quellenverzeichnis mit Links

---

## Notion-IDs

| Objekt | ID |
|--------|-----|
| Teaching Methods (Seite) | `2fb85cf5-9b35-8037-988e-f517771838eb` |
| Methoden-Datenbank (DB) | `2f14bea1-b1a9-4bbe-a018-948d164ce230` |
| Methoden-Datenbank (DS) | `4ec53dc6-82e9-4a24-96fb-970114ed2548` |

---

## Workflow

1. Tom schickt Paper-Link (Sci-Hub, DOI, PDF)
2. Aether lädt & liest das Paper
3. Aether erstellt:
   a. Paper-Zusammenfassung in Notion (These/Methode/Erkenntnis/Kritik/Praxis)
   b. Methoden-DB-Eintrag mit allen Feldern + Praxisrelevanz
   c. Lokale MD-Dateien als Backup
4. Tom sieht alles schön aufbereitet in Notion auf dem iPad ✨
