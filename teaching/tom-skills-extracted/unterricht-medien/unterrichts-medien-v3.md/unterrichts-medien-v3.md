---
name: unterrichts-medien
description: Erstellt Bilder, Grafiken, Infografiken und einfache Visualisierungen für Unterrichtsmaterialien mittels ComfyUI (lokal) oder Fallback-Optionen. Nutze bei Anfragen nach Bildmaterial, Illustrationen, Charts, Infografiken oder visuellen Materialien für den Unterricht.
---

# Unterrichts-Medien Skill v3.1

Erstellt visuelle Unterrichtsmaterialien über ComfyUI (lokal bevorzugt) oder Fallback-Systeme.

**NEU in v3.1:** Robusterer ComfyUI-Workflow mit Retry-Logik, Integration mit PPTX-Design-System

---

## ⚠️ PFLICHT-CHECK VOR BILDGENERIERUNG

```
┌─────────────────────────────────────────────────────────────────┐
│  🚨 STOP! BEVOR DU BILDER GENERIERST:                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. Ist ComfyUI verfügbar?                                      │
│     ├── Prüfen mit osascript (curl)                             │
│     ├── Falls nicht → Starten mit osascript                     │
│     └── 5-10 Sek. warten → erneut prüfen                        │
│                                                                 │
│  2. Für welchen Zweck?                                          │
│     ├── PPTX-Folie → 16:9 (1920x1080 oder 1024x576)             │
│     ├── Arbeitsblatt → 1:1 oder 4:3                             │
│     └── Bildkarten → 1:1 (1024x1024)                            │
│                                                                 │
│  3. FLUX-Prompt korrekt?                                        │
│     ├── KEINE Quality Tags ("masterpiece", etc.)                │
│     ├── KEINE Künstlernamen                                     │
│     └── Struktur: Subject → Action → Style → Technical          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## When to Use This Skill

**Trigger-Wörter:**
- "Bild erstellen", "Grafik", "Illustration"
- "Infografik", "Chart", "Diagramm"
- "Bildimpuls", "Visual", "Poster"
- "Bildkarten", "Flashcards"
- Handover enthält Bild-Prompts oder Bildanforderungen
- PPTX-Erstellung benötigt visuelle Elemente

**Nicht verwenden für:**
- Komplexe Datenvisualisierungen (nutze Excel/Charts)
- Fotografien mit echten Personen
- Urheberrechtlich geschützte Charaktere
- Mermaid-Diagramme (nutze Mermaid Chart MCP)

---

## Verfügbare Tools (Prioritätsreihenfolge)

### 🥇 ComfyUI (LOKAL - PRIMÄR)

**Setup:**
- Lokale Installation: `~/ComfyUI`
- Modell: FLUX.1-schnell (GGUF Q4_0, ~6.4 GB)
- Läuft auf: `http://127.0.0.1:8188`
- MCP Server: `comfyui-mcp-server`

**Tool-Name:** `comfyui:generate_image`

**Vorteile:**
- ✅ Schnell & kostenlos
- ✅ Offline verfügbar
- ✅ Hohe Qualität (FLUX.1-schnell)
- ✅ Volle Kontrolle
- ✅ Keine API-Limits
- ✅ Apache 2.0 Lizenz (kommerziell nutzbar)

---

## ⚡ COMFYUI AUTO-START WORKFLOW (v3.1)

Da Cowork in einer isolierten VM läuft, muss ComfyUI über **osascript** auf dem Host gestartet werden.

### Vollständiger Workflow mit Retry-Logik

```
┌─────────────────────────────────────────────────────────────────┐
│ SCHRITT 1: Prüfe ob ComfyUI läuft                               │
├─────────────────────────────────────────────────────────────────┤
│ Control your Mac:osascript                                       │
│ script: 'do shell script "curl -s -m 5                           │
│          http://127.0.0.1:8188/system_stats"'                    │
│                                                                 │
│ ✅ Erfolg: JSON mit "comfyui_version" → Weiter zu Schritt 4     │
│ ❌ Fehler: "Connection refused" / Code 7 → Weiter zu Schritt 2  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ SCHRITT 2: Starte ComfyUI auf Host                              │
├─────────────────────────────────────────────────────────────────┤
│ Control your Mac:osascript                                       │
│ script: 'do shell script "cd ~/ComfyUI &&                        │
│          source venv/bin/activate &&                             │
│          python main.py --use-pytorch-cross-attention            │
│          --force-fp16 &> /tmp/comfyui.log &\necho started"'      │
│                                                                 │
│ ⚠️ WICHTIG: Befehl MUSS mit "&> ... &\necho started" enden!     │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ SCHRITT 3: Warte auf Start (5-10 Sekunden)                      │
├─────────────────────────────────────────────────────────────────┤
│ Control your Mac:osascript                                       │
│ script: 'delay 8'                                                │
│                                                                 │
│ Dann erneut Schritt 1 ausführen zur Bestätigung                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ SCHRITT 4: Bild generieren                                      │
├─────────────────────────────────────────────────────────────────┤
│ comfyui:generate_image                                          │
│ prompt: "[FLUX-optimierter Prompt]"                              │
│ width: 1024                                                      │
│ height: 1024 (oder 576 für 16:9)                                 │
│ seed: -1 (oder fester Wert für Serien)                          │
└─────────────────────────────────────────────────────────────────┘
```

### Code-Snippets zum Kopieren

**1. ComfyUI Status prüfen:**
```javascript
Control your Mac:osascript({
  script: 'do shell script "curl -s -m 5 http://127.0.0.1:8188/system_stats"'
})
```

**2. ComfyUI starten (wenn nicht läuft):**
```javascript
Control your Mac:osascript({
  script: 'do shell script "cd ~/ComfyUI && source venv/bin/activate && python main.py --use-pytorch-cross-attention --force-fp16 &> /tmp/comfyui.log &\necho started"'
})
```

**3. Warten (AppleScript delay):**
```javascript
Control your Mac:osascript({
  script: 'delay 8'
})
```

**4. Bild generieren:**
```javascript
comfyui:generate_image({
  prompt: "Medieval peasant working in fields, historical illustration, 14th century clothing, educational material, f/8 sharp focus",
  width: 1024,
  height: 1024,
  seed: -1
})
```

---

### 🥈 Nanobanana (Google Gemini - BACKUP)

**Tool-Name:** `nanobanana:generate_image`

**Parameter:**
- `prompt`: Bildbeschreibung
- `aspect_ratio`: "1:1", "16:9", "3:4", etc.
- `model`: "pro" oder "normal"
- `output_path`: Absoluter Pfad zum Speichern

**Verwendung:**
```javascript
nanobanana:generate_image({
  prompt: "[Prompt]",
  aspect_ratio: "16:9",
  model: "pro",
  output_path: "/Users/tomren/Desktop/image.png"
})
```

### 🥉 Hugging Face Spaces (FALLBACK)

**1. FLUX.1 Kontext (Bearbeitung existierender Bilder)**
```javascript
Hugging Face:gr1_flux_1_kontext_dev_infer({
  prompt: "[Bearbeitungsanweisung]",
  input_image: "[URL oder Pfad]",
  guidance_scale: 2.5,
  steps: 28
})
```

**2. Z-Image Turbo (Schnelle Generierung)**
```javascript
Hugging Face:gr4_z_image_turbo_generate({
  prompt: "[Prompt]",
  resolution: "1024x1024 ( 1:1 )",  // Format mit Leerzeichen!
  steps: 8
})
```

**⚠️ Beachte:** Resolution muss im Format `"1024x1024 ( 1:1 )"` mit Leerzeichen angegeben werden!

---

## Automatischer Fallback-Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. Versuche: comfyui:generate_image                             │
├─────────────────────────────────────────────────────────────────┤
│ Erfolg? → Bild generiert ✅                                     │
│ Fehler "Cannot connect to host 127.0.0.1:8188"?                 │
│         ↓                                                       │
│ 2. Starte ComfyUI via osascript                                 │
│         ↓                                                       │
│ 3. Warte 8 Sekunden (delay)                                     │
│         ↓                                                       │
│ 4. Versuche erneut: comfyui:generate_image                      │
│         ↓                                                       │
│ Erfolg? → Bild generiert ✅                                     │
│ Fehler? → Fallback zu Nanobanana/HuggingFace                    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Integration mit PPTX Design-System

### Farbabstimmung (aus unterrichtsstunde-erstellen-v3)

```javascript
const PPTX_COLORS = {
  DARK_BLUE: "1E3A5F",      // Für Bildrahmen, Text-Overlays
  ACCENT_RED: "C00000",     // Akzente
  LIGHT_GRAY: "F5F5F5",     // Hintergründe
  CRISIS_ORANGE: "D35400",  // Krisen-Themen
  CRISIS_YELLOW: "F39C12",  // Warnungen
  CRISIS_BLUE: "2980B9",    // Info-Themen
};
```

### Aspektverhältnisse für PPTX

| Verwendung | Verhältnis | Auflösung | Prompt-Suffix |
|------------|------------|-----------|---------------|
| Vollbild-Folie | 16:9 | 1920x1080 oder 1024x576 | - |
| Halbe Folie | 16:9 | 1024x576 | - |
| Quadratisches Element | 1:1 | 1024x1024 | - |
| Hochformat-Insert | 3:4 | 768x1024 | - |

### Prompt-Suffix für PPTX-Bilder

Füge bei Bildern für Präsentationen hinzu:
```
..., high contrast for projection, bright colors, clean composition, f/8 sharp focus
```

---

## FLUX Prompting Best Practices (Black Forest Labs)

### Grund-Struktur:
```
Subject → Action → Environment → Lighting → Style/Modifiers
```

### ✅ Do's:
- **Natürliche Sprache** verwenden (40-50 Wörter optimal)
- **Konkrete Aktionen** beschreiben: "running", "sitting", "celebrating"
- **Beleuchtung spezifizieren**: "golden hour lighting", "studio lighting"
- **Foto-Parameter** für Realismus: "f/8 sharp focus", "85mm lens"
- **Text in Anführungszeichen**: `"The text 'OPEN' in red letters"`

### ❌ Don'ts:
- **KEINE Quality Tags**: "masterpiece", "best quality", "highly detailed" (unnötig!)
- **KEINE Künstlernamen**: FLUX kennt keine spezifischen Künstler (EU-Recht)
- Stattdessen: **Stil-Beschreibungen** wie "Van Gogh painting style with swirling brushstrokes"
- **Keine Keyword-Listen**: Vermeide zufällige Aneinanderreihung

---

## Prompt-Templates für Unterrichtsmaterialien (FLUX-optimiert)

### Kindgerechte Illustrationen
```
[MOTIV] [AKTION/SITUATION], photorealistic style,
bright cheerful colors with high contrast, simple clean composition,
educational material, f/8 sharp focus
```

### Infografiken
```
[THEMA] infographic, educational diagram with simple icons,
pastel colors with clear visual hierarchy, minimalist design,
high contrast, f/8 sharp focus
```

### Historische Szenen (Geschichte)
```
[EPOCHE] [SZENE], historical illustration style,
period-accurate clothing and architecture, educational material,
muted earth tones, detailed but clear composition, f/8 sharp focus
```

**Beispiel Mittelalter:**
```
Medieval European village market scene with peasants and merchants,
historical illustration style, period-accurate 14th century clothing,
timber-framed buildings, educational material,
muted earth tones, detailed but clear composition, f/8 sharp focus
```

### Emotionen/Situationen (Sprachunterricht)
```
[PERSON/TIER] showing [EMOTION], photorealistic style,
expressive face with clear emotion, solid color background,
educational flashcard, f/8 sharp focus
```

### Quellenbilder (Geschichte)
```
[HISTORISCHES DOKUMENT/KUNSTWERK] style recreation,
period-accurate [EPOCHE] artistic style, aged parchment texture,
educational reproduction, high contrast, f/8 sharp focus
```

**Beispiel Holzschnitt:**
```
Medieval woodcut print showing three estates of society,
clergy nobility and peasants in hierarchical arrangement,
black and white woodcut style with fine line details,
15th century German artistic style, educational material, f/8 sharp focus
```

### Politikunterricht / Demokratie
```
[POLITISCHES KONZEPT] visualized as [METAPHER/SYMBOL],
clean modern illustration style, bold flat colors,
infographic aesthetic, educational material, high contrast, f/8 sharp focus
```

**Beispiel Gewaltenteilung:**
```
Three pillars representing separation of powers,
legislative executive and judicial branches as distinct columns,
clean modern illustration style, blue and gold colors,
infographic aesthetic, educational material, high contrast, f/8 sharp focus
```

### Karikaturen-Stil (für Politik/Geschichte)
```
[THEMA] as political cartoon in [EPOCHE] style,
exaggerated features, satirical tone, black ink drawing style,
cross-hatching details, educational material, high contrast
```

---

## Workflow für Bildgenerierung

### Schritt 1: Anforderung analysieren
- Was zeigt das Bild?
- Für welche Altersgruppe?
- Beamer-Projektion oder Arbeitsblatt?
- Farbig oder schwarz-weiß?
- Welches Aspektverhältnis? (16:9 für PPTX, 1:1 für Karten)

### Schritt 2: ComfyUI Status prüfen & ggf. starten

```javascript
// Prüfen
Control your Mac:osascript({
  script: 'do shell script "curl -s -m 5 http://127.0.0.1:8188/system_stats"'
})

// Bei Fehler: Starten
Control your Mac:osascript({
  script: 'do shell script "cd ~/ComfyUI && source venv/bin/activate && python main.py --use-pytorch-cross-attention --force-fp16 &> /tmp/comfyui.log &\necho started"'
})

// Warten
Control your Mac:osascript({
  script: 'delay 8'
})
```

### Schritt 3: Prompt formulieren
- Nutze FLUX-optimiertes Template von oben
- Ergänze spezifische Details
- Füge Beleuchtung hinzu wenn relevant
- Struktur: Subject → Action → Style → Technical
- Für PPTX: "high contrast for projection" hinzufügen

### Schritt 4: Bild generieren
```javascript
comfyui:generate_image({
  prompt: "[FLUX-optimierter Prompt]",
  width: 1024,
  height: 576,  // 16:9 für PPTX
  seed: -1
})
```

### Schritt 5: In PPTX einbetten (falls nötig)
Siehe `unterrichtsstunde-erstellen-v3` für Integration.

---

## FLUX.1-schnell Spezifika

### Modell-Eigenschaften:
- **Steps:** 1-4 optimal (sehr schnell!)
- **Lizenz:** Apache 2.0 (kommerziell nutzbar)
- **Stärken:** Schnelle Generierung bei guter Qualität
- **Fotografie-Parameter:**
  - `f/1.4` = unscharfer Hintergrund (Bokeh)
  - `f/8` = alles scharf (empfohlen für Bildungsmaterialien)
  - `85mm lens` = Portrait
  - `24mm` = Weitwinkel

### Text in Bildern:
```
"The text 'VOCABULARY' appears in bold letters at the top",
centered, elegant sans-serif typography
```

---

## Batch-Generierung für Serien

### Konsistenter Stil mit festem Seed

Für Bildserien (z.B. 6 Emotionskarten):

```javascript
const BASE_SEED = 12345;  // Fester Ausgangspunkt

const emotions = ["happy", "sad", "angry", "surprised", "confused", "excited"];

emotions.forEach((emotion, index) => {
  comfyui:generate_image({
    prompt: `Young child showing ${emotion} emotion with expressive face,
      photorealistic style, solid pastel background,
      educational flashcard, f/8 sharp focus`,
    width: 1024,
    height: 1024,
    seed: BASE_SEED + index  // Konsistente aber verschiedene Seeds
  });
});
```

### Stil-Konsistenz-Suffix

Für alle Bilder einer Einheit den gleichen Suffix verwenden:
```
..., consistent illustration style, educational material series,
bright colors, clean composition, f/8 sharp focus
```

---

## Qualitätsrichtlinien

### Do's ✓
- Einfache, klare Kompositionen
- Helle, freundliche Farben
- Hoher Kontrast für Beamer (`high contrast`)
- Kindgerechte Darstellungen
- Diversität bei Personen
- Konsistenter Stil innerhalb einer Einheit (gleicher Seed)
- FLUX-Struktur: Subject → Action → Style

### Don'ts ✗
- Keine echten Personen/Fotos-Referenzen
- Keine urheberrechtlich geschützten Charaktere
- Keine Künstlernamen (stattdessen Stil-Beschreibungen)
- Keine Quality Tags ("masterpiece", "best quality")
- Kein Text im Bild ohne Anführungszeichen
- Keine zu komplexen Szenen
- Keine gruseligen/beängstigenden Elemente
- Keine stereotypen Darstellungen

---

## Beispiel-Workflows

### Beispiel 1: Bildimpuls "Mittelalter Ständegesellschaft"
```javascript
// 1. ComfyUI prüfen/starten (siehe oben)

// 2. Generieren (16:9 für PPTX)
comfyui:generate_image({
  prompt: `Medieval three estates pyramid showing clergy at top,
    nobility in middle, peasants at bottom working the fields,
    historical illustration style with period-accurate 14th century details,
    educational diagram, muted earth tones, high contrast for projection,
    f/8 sharp focus`,
  width: 1024,
  height: 576,
  seed: -1
})
```

### Beispiel 2: Emotionskarte "Happy"
```javascript
comfyui:generate_image({
  prompt: `Young child showing happiness with wide smile,
    photorealistic style, expressive face with clear emotion,
    solid yellow background, educational flashcard, f/8 sharp focus`,
  width: 1024,
  height: 1024,
  seed: 12345  // Fester Seed für Serie
})
```

### Beispiel 3: Holzschnitt-Stil für Geschichte
```javascript
comfyui:generate_image({
  prompt: `Medieval woodcut print showing feudal hierarchy,
    king on throne with nobles and clergy surrounding,
    peasants working below, black and white woodcut style,
    fine crosshatch lines, 15th century German artistic style,
    educational material, high contrast`,
  width: 1024,
  height: 768,
  seed: -1
})
```

### Beispiel 4: Politikbild "Demokratie"
```javascript
comfyui:generate_image({
  prompt: `Citizens casting votes at ballot boxes in modern setting,
    diverse group of people participating in democracy,
    clean modern illustration style, blue and warm colors,
    civic engagement theme, educational material,
    high contrast for projection, f/8 sharp focus`,
  width: 1024,
  height: 576,
  seed: -1
})
```

---

## Integration mit anderen Skills

### Mit arbeitsblatt-erstellen-v3:
1. Bild mit ComfyUI generieren
2. Bild speichern
3. Im Arbeitsblatt referenzieren
4. Bild separat ausdrucken oder digital zeigen

### Mit unterrichtsstunde-erstellen-v3 / pptx:
1. Bilder für Bildimpulse mit ComfyUI generieren (16:9!)
2. In PowerPoint als Folien einfügen
3. Design-System-Farben für Rahmen/Overlays nutzen
4. Dateinamen notieren für Referenz

### Mit unterrichtsplanung-workflow:
1. Handover enthält Bild-Anforderungen
2. Dieser Skill wird automatisch getriggert
3. Bilder werden generiert und in Materialübersicht eingetragen

---

## Fehlerbehebung

### Problem: ComfyUI MCP Tool verbindet nicht
**Ursache:** Cowork VM kann Host-localhost nicht direkt erreichen.

**Lösung:** Starte ComfyUI über osascript:
```javascript
Control your Mac:osascript({
  script: 'do shell script "cd ~/ComfyUI && source venv/bin/activate && python main.py --use-pytorch-cross-attention --force-fp16 &> /tmp/comfyui.log &\necho started"'
})
```

### Problem: osascript blockiert/Timeout
**Ursache:** Befehl ohne Background-Operator `&`

**Lösung:** Befehl MUSS mit `&> /tmp/comfyui.log &\necho started` enden!

### Problem: ComfyUI startet aber Tool findet es nicht
**Ursache:** Zu wenig Wartezeit

**Lösung:** Warte 8-10 Sekunden mit `delay 8` vor erneutem Versuch

### Problem: Bild hat unerwünschten Text
**Lösung:** Füge "no text in image, no words, no letters" zum Prompt hinzu

### Problem: Bild zu komplex
**Lösung:** Reduziere Elemente im Prompt, nutze "simple composition, minimalist"

### Problem: Farben zu dunkel für Beamer
**Lösung:** Füge "bright colors, high contrast for projection, f/8 sharp focus" hinzu

### Problem: Stil inkonsistent zwischen Bildern
**Lösung:** Nutze identischen Stil-Suffix für alle Bilder einer Serie, verwende **gleichen Seed**

### Problem: Alle Tools schlagen fehl
**Lösung:** Fallback-Kette durchlaufen:
1. ComfyUI erneut versuchen (nach Neustart)
2. Nanobanana (Google Gemini)
3. HuggingFace Z-Image Turbo

---

## Checkliste für Bildgenerierung

- [ ] ComfyUI Status geprüft (osascript curl)
- [ ] ComfyUI gestartet falls nötig (osascript start)
- [ ] 8 Sekunden gewartet (delay)
- [ ] Prompt folgt FLUX-Struktur: Subject → Action → Style
- [ ] KEINE Quality Tags verwendet
- [ ] KEINE Künstlernamen verwendet
- [ ] Richtiges Aspektverhältnis (16:9 für PPTX, 1:1 für Karten)
- [ ] Stil ist altersgerecht
- [ ] Keine urheberrechtlichen Probleme
- [ ] Hoher Kontrast für Projektion (`high contrast for projection`)
- [ ] Dateiname folgt Konvention
- [ ] Bild im korrekten Ordner gespeichert

---

## Quick Reference

**ComfyUI Status prüfen:**
```javascript
Control your Mac:osascript({ script: 'do shell script "curl -s -m 5 http://127.0.0.1:8188/system_stats"' })
```

**ComfyUI starten:**
```javascript
Control your Mac:osascript({ script: 'do shell script "cd ~/ComfyUI && source venv/bin/activate && python main.py --use-pytorch-cross-attention --force-fp16 &> /tmp/comfyui.log &\necho started"' })
```

**Warten:**
```javascript
Control your Mac:osascript({ script: 'delay 8' })
```

**Bild generieren (PPTX 16:9):**
```javascript
comfyui:generate_image({ prompt: "[...]", width: 1024, height: 576, seed: -1 })
```

**Bild generieren (Quadrat):**
```javascript
comfyui:generate_image({ prompt: "[...]", width: 1024, height: 1024, seed: -1 })
```

**Tool-Priorität:**
1. `comfyui:generate_image` (lokal, schnell)
2. `nanobanana:generate_image` (Google Gemini)
3. `Hugging Face:gr4_z_image_turbo_generate` (HuggingFace)

**Basis-Prompt-Struktur:**
```
[Subject] [Action], [Style], [Details], [Lighting], [Technical: f/8 sharp focus]
```

**PPTX-Suffix:**
```
..., high contrast for projection, bright colors, clean composition, f/8 sharp focus
```

---

## Changelog

| Version | Datum | Änderungen |
|---------|-------|------------|
| 3.1.0 | 27.01.2026 | **Robusterer Workflow mit Retry-Logik**; PPTX-Design-System-Integration; Aspektverhältnisse für PPTX; Batch-Generierung; Politikbild-Templates; curl timeout Parameter |
| 3.0.0 | 27.01.2026 | Auto-Start ComfyUI via osascript; getesteter Workflow für Cowork-VM; vollständige MCP-Tool-Namen; historische Prompt-Templates |
| 2.0.0 | 20.01.2026 | FLUX-optimierte Prompts |
| 1.0.0 | 15.01.2026 | Initial Release |

---

*Version: 3.1.0 - Robuster Workflow + PPTX-Integration*
*Erstellt: Januar 2026*
*Abhängigkeit: ComfyUI (primär), Nanobanana/Hugging Face (Fallback)*
*Modell: FLUX.1-schnell (Black Forest Labs)*
*Integration: unterrichtsstunde-erstellen-v3, arbeitsblatt-erstellen-v3*
