# Holocaust-Stunde v2: "Entscheidungen 1933-1945"

**Erstellt**: 2026-02-03  
**Klasse**: 2BFH2-GGK  
**Fach**: GGK  
**Dauer**: 90 Minuten  
**BPE**: 2.1 (Nationalsozialismus)

---

## 📦 Erstellte Materialien

### ✅ Vollständig einsatzbereit:

1. **Stundenplanung.md** — Detaillierte Ablaufplanung (90 Min., 5 Phasen)
2. **Stunde_01_PPT.pptx** — PowerPoint-Präsentation (10 Folien, dunkles Design, 16:9)
3. **doc/AB_01_Entscheidungen.docx** — Arbeitsblatt (3 Seiten, Niveau C, Scaffolding eingebaut)
4. **TQF_Kurzcheck.md** — Qualitätsbewertung nach Teaching Quality Framework (4.8/5 Sterne)

---

## 🖼️ Bilder (manuell hinzufügen)

**Folie 2**: Historisches Foto einfügen

Da kein HuggingFace Token verfügbar war, müssen folgende Bilder **manuell** hinzugefügt werden:

### Bild 1: Historisches Foto (Folie 2 der PowerPoint)
**Empfehlung**: Originalfoto von 1933 verwenden (frei verfügbar z.B. über Bundesarchiv)

**Suchbegriffe**:
- "Judenboykott 1933"
- "Boycott of Jewish businesses April 1 1933"
- "SA vor jüdischem Geschäft 1933"

**Quellen**:
- Bundesarchiv: https://www.bild.bundesarchiv.de/
- United States Holocaust Memorial Museum: https://www.ushmm.org/
- Wikimedia Commons: https://commons.wikimedia.org/

**Wichtig**: 
- Lizenz prüfen (oft gemeinfrei für Bildungszwecke)
- Bildquelle angeben (z.B. "Bundesarchiv, Bild 102-14468 / Georg Pahl / CC-BY-SA 3.0")

### Bild einfügen in PowerPoint:
1. PowerPoint öffnen (`Stunde_01_PPT.pptx`)
2. Folie 2 anklicken
3. "Einfügen" → "Bilder" → Bild auswählen
4. Größe anpassen (ca. 6x4 Zoll, zentriert unter Titel)
5. Bildunterschrift hinzufügen: "Boykott jüdischer Geschäfte, 1. April 1933 (Quelle: ...)"

---

## 🎮 Mammutprojekt-Prototypen

Die Stunde nutzt interaktive Prototypen auf iPads:

- **David-Perspektive** (Opfer): `/teaching/mammutprojekt/prototype/david-perspective.html`
- **Werner-Perspektive** (Zuschauer): `/teaching/mammutprojekt/prototype/index.html`

**Vorbereitung**:
- [ ] iPads aufladen (1:1 oder 1:2)
- [ ] Links testen (auf iPad öffnen, Funktionalität prüfen)
- [ ] Optional: QR-Codes erstellen für schnellen Zugriff
  - QR-Code-Generator: https://www.qr-code-generator.com/
  - Ausdrucken und auf Tische legen

---

## 📋 Checkliste vor der Stunde

### Technik:
- [ ] iPads aufgeladen und bereit (mind. 1 pro 2 SuS)
- [ ] Mammutprojekt-Links funktionieren
- [ ] PowerPoint auf Lehrerrechner geladen
- [ ] Beamer/Smartboard funktioniert

### Materialien:
- [ ] Arbeitsblätter ausgedruckt (1x pro SuS, 3 Seiten)
- [ ] Exit-Ticket-Karten bereit (Karteikarten oder kleine Zettel)
- [ ] Evtl. QR-Codes für Prototypen ausgedruckt

### Raum:
- [ ] Tische für Partnerarbeit arrangierbar
- [ ] Tafel/Whiteboard frei für Tafelanschrieb (Phase 1)

---

## 🎯 Kernkonzept der Stunde

**Leitfrage**: "Wie konnte es dazu kommen, dass normale Menschen zuschauten?"

**Methode**: Spielbasiertes Lernen mit Perspektivwechsel

**5 Phasen**:
1. **Einstieg** (15 Min.): Historisches Foto → Stilles Schreiben → Leitfrage
2. **Hauptteil** (35 Min.): Mammutprojekt spielen (David ODER Werner) mit Self-Explanation
3. **Perspektivwechsel** (15 Min.): Partnerarbeit David ↔ Werner
4. **Reflexion** (20 Min.): Stilles Schreiben "Und ich?" → Gegenwartsbezug
5. **Sicherung** (5 Min.): Exit-Ticket → Ausblick nächste Stunde

---

## 📊 TQF-Bewertung

**Gesamtbewertung**: ★★★★★ (4.8/5) — Exzellent

| Dimension | Bewertung | Kommentar |
|-----------|-----------|-----------|
| 1. Lernziele & Kompetenzorientierung | ★★★★★ | Klare Leitfrage, dreistufige Lernziele |
| 2. Unterrichtsstruktur & Methodik | ★★★★★ | Innovative spielbasierte Methode, strukturiert |
| 3. Lernunterstützung & Differenzierung | ★★★★☆ | Scaffolding für alle, freie Perspektivenwahl |
| 4. Kognitive Aktivierung | ★★★★★ | Self-Explanation, moralische Dilemmata |
| 5. Lernklima & Emotionale Sicherheit | ★★★★★ | Sensibel, freiwilliges Vorlesen, geschützter Raum |

**Stärken**:
- Innovative Methode (Mammutprojekt)
- Strukturierter Perspektivwechsel
- Metakognitive Tiefe (Self-Explanation)
- Emotionale Sicherheit

**Entwicklungspotenzial**:
- Backup-Plan bei technischen Problemen
- Optionale Vertiefung für leistungsstarke SuS

---

## 📂 Dateistruktur

```
Holocaust_v2/
├── README.md                      ← Diese Datei
├── Stundenplanung.md             ← Ablaufplan (90 Min.)
├── Stunde_01_PPT.pptx            ← PowerPoint-Präsentation (10 Folien)
├── TQF_Kurzcheck.md              ← Qualitätsbewertung
├── doc/
│   └── AB_01_Entscheidungen.docx ← Arbeitsblatt (3 Seiten)
├── images/                        ← (leer, Bilder manuell hinzufügen)
├── create_ppt.py                 ← Skript für PPT-Erstellung
├── create_arbeitsblatt.py        ← Skript für AB-Erstellung
└── ppt_config.json               ← Konfiguration (nicht verwendet)
```

---

## 🚀 Schnellstart

1. **Materialien drucken**: `doc/AB_01_Entscheidungen.docx` ausdrucken (1x pro SuS)
2. **Bild hinzufügen**: Historisches Foto in `Stunde_01_PPT.pptx` (Folie 2) einfügen
3. **Technik testen**: iPads laden, Links prüfen
4. **PowerPoint bereit**: `Stunde_01_PPT.pptx` auf Lehrerrechner
5. **Los geht's!** 🎓

---

## 📞 Support

Bei Fragen oder Problemen:
- Stundenplanung lesen (alle Details dort)
- TQF-Kurzcheck für didaktische Begründung
- Mammutprojekt-Links testen vor der Stunde

**Viel Erfolg!** 💪
