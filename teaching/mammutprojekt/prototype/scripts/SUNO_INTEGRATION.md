# Suno Integration - Versuchsprotokoll

**Datum:** 2026-02-02
**Ziel:** Automatische Musik-Generierung via Suno.ai für Mammutprojekt

---

## Versuch 1: Unoffizielle Python Libraries

### SunoAI (pip install SunoAI)
- **Status:** ❌ Fehlgeschlagen
- **Fehler:** `Failed to get Session ID: 200`
- **Grund:** Library erwartet anderes Cookie-Format

### suno-api (pip install suno-api)
- **Status:** ❌ Fehlgeschlagen  
- **Fehler:** API-Endpoint gibt "Service Suspended" zurück
- **Grund:** Suno hat inoffizielle API-Zugriffe blockiert

---

## Versuch 2: Playwright Browser-Automation

### Setup
- Playwright installiert: ✅
- Chromium Headless Shell: ✅ (145.0.7632.6)

### Probleme & Lösungen

(wird während der Tests aktualisiert)

---

## Cookie-Informationen

**Benötigte Cookies von suno.com:**
- `__session` (JWT Token, ~1.1KB)
- Weitere Auth-Cookies möglicherweise nötig

**Cookie-Lebensdauer:** ~1 Jahr (laut Screenshot)

---

## Nächste Schritte

1. [ ] Playwright-Script mit Cookie-Injection testen
2. [ ] Login-Status prüfen
3. [ ] Create-Seite navigieren
4. [ ] Prompt eingeben und generieren
5. [ ] Download der generierten Musik
6. [ ] Fehler dokumentieren

---

## Log

**[19:20:53]** 🚀 Starte Playwright Browser-Automation

**[19:20:53]** ✅ Cookie geladen (1166 Zeichen)

**[19:20:54]** 📦 Starte Chromium (headless)...

**[19:20:54]** ❌ Browser-Start fehlgeschlagen: BrowserType.launch: Target page, context or browser has been closed
Browser logs:

<launching> /root/.cache/ms-playwright/chromium_headless_shell-1208/chrome-headless-shell-linux64/chrome-headless-shell --disable-field-trial-config --disable-background-networking --disable-background-timer-throttling --disable-backgrounding-occluded-windows --disable-back-forward-cache --disable-breakpad --disable-client-side-phishing-detection --disable-component-extensions-with-background-pages --disable-component-update --no-default-browser-check --disable-default-apps --disable-dev-shm-usage --disable-extensions --disable-features=AvoidUnnecessaryBeforeUnloadCheckSync,BoundaryEventDispatchTracksNodeRemoval,DestroyProfileOnBrowserClose,DialMediaRouteProvider,GlobalMediaControls,HttpsUpgrades,LensOverlay,MediaRouter,PaintHolding,ThirdPartyStoragePartitioning,Translate,AutoDeElevate,RenderDocument,OptimizationHints --enable-features=CDPScreenshotNewSurface --allow-pre-commit-input --disable-hang-monitor --disable-ipc-flooding-protection --disable-popup-blocking --disable-prompt-on-repost --disable-renderer-backgrounding --force-color-profile=srgb --metrics-recording-only --no-first-run --password-store=basic --use-mock-keychain --no-service-autorun --export-tagged-pdf --disable-search-engine-choice-screen --unsafely-disable-devtools-self-xss-warnings --edge-skip-compat-layer-relaunch --enable-automation --disable-infobars --disable-search-engine-choice-screen --disable-sync --enable-unsafe-swiftshader --headless --hide-scrollbars --mute-audio --blink-settings=primaryHoverType=2,availableHoverTypes=2,primaryPointerType=4,availablePointerTypes=4 --no-sandbox --no-sandbox --disable-dev-shm-usage --user-data-dir=/tmp/playwright_chromiumdev_profile-xBD2Sw --remote-debugging-pipe --no-startup-window
<launched> pid=85036
[pid=85036][err] /root/.cache/ms-playwright/chromium_headless_shell-1208/chrome-headless-shell-linux64/chrome-headless-shell: error while loading shared libraries: libatk-1.0.so.0: cannot open shared object file: No such file or directory
Call log:
  - <launching> /root/.cache/ms-playwright/chromium_headless_shell-1208/chrome-headless-shell-linux64/chrome-headless-shell --disable-field-trial-config --disable-background-networking --disable-background-timer-throttling --disable-backgrounding-occluded-windows --disable-back-forward-cache --disable-breakpad --disable-client-side-phishing-detection --disable-component-extensions-with-background-pages --disable-component-update --no-default-browser-check --disable-default-apps --disable-dev-shm-usage --disable-extensions --disable-features=AvoidUnnecessaryBeforeUnloadCheckSync,BoundaryEventDispatchTracksNodeRemoval,DestroyProfileOnBrowserClose,DialMediaRouteProvider,GlobalMediaControls,HttpsUpgrades,LensOverlay,MediaRouter,PaintHolding,ThirdPartyStoragePartitioning,Translate,AutoDeElevate,RenderDocument,OptimizationHints --enable-features=CDPScreenshotNewSurface --allow-pre-commit-input --disable-hang-monitor --disable-ipc-flooding-protection --disable-popup-blocking --disable-prompt-on-repost --disable-renderer-backgrounding --force-color-profile=srgb --metrics-recording-only --no-first-run --password-store=basic --use-mock-keychain --no-service-autorun --export-tagged-pdf --disable-search-engine-choice-screen --unsafely-disable-devtools-self-xss-warnings --edge-skip-compat-layer-relaunch --enable-automation --disable-infobars --disable-search-engine-choice-screen --disable-sync --enable-unsafe-swiftshader --headless --hide-scrollbars --mute-audio --blink-settings=primaryHoverType=2,availableHoverTypes=2,primaryPointerType=4,availablePointerTypes=4 --no-sandbox --no-sandbox --disable-dev-shm-usage --user-data-dir=/tmp/playwright_chromiumdev_profile-xBD2Sw --remote-debugging-pipe --no-startup-window
  - <launched> pid=85036
  - [pid=85036][err] /root/.cache/ms-playwright/chromium_headless_shell-1208/chrome-headless-shell-linux64/chrome-headless-shell: error while loading shared libraries: libatk-1.0.so.0: cannot open shared object file: No such file or directory
  - [pid=85036] <gracefully close start>
  - [pid=85036] <kill>
  - [pid=85036] <will force kill>
  - [pid=85036] exception while trying to kill process: Error: kill ESRCH
  - [pid=85036] <process did exit: exitCode=127, signal=null>
  - [pid=85036] starting temporary directories cleanup
  - [pid=85036] finished temporary directories cleanup
  - [pid=85036] <gracefully close end>


### 19:20 - Browser-Start Problem

**Fehler:** `error while loading shared libraries: libatk-1.0.so.0`

**Ursache:** Chromium headless braucht GUI-Libraries auch im headless mode

**Lösung:** `playwright install-deps chromium` (läuft gerade)

**Betroffene Pakete:**
- libatk-1.0.so.0 (ATK accessibility toolkit)
- Weitere GUI-Libraries wahrscheinlich auch


**[19:21:30]** 🚀 Starte Playwright Browser-Automation

**[19:21:30]** ✅ Cookie geladen (1166 Zeichen)

**[19:21:30]** 📦 Starte Chromium (headless)...

**[19:21:31]** ✅ Browser gestartet

**[19:21:31]** 🍪 Setze Session-Cookie...

**[19:21:31]** ✅ Cookie gesetzt

**[19:21:31]** 🌐 Navigiere zu suno.com...

**[19:22:01]** ❌ Navigation fehlgeschlagen: Page.goto: Timeout 30000ms exceeded.
Call log:
  - navigating to "https://suno.com/", waiting until "networkidle"


### 19:42 - Cookie-Analyse

**Cookies getestet:**

1. `__session` (Access Token)
   - Typ: `access`
   - Ablauf: 2026-02-02 20:11 (kurz!)
   - Audience: `suno-api`
   
2. `__session_Jnxw-muT` (Refresh Token)
   - Typ: `refresh`
   - Ablauf: 2027-02-02 (1 Jahr!)
   - Client: `client_xgJ6byU4N4MjTY3aeQFJJx`

**Problem:** Beide Tokens zusammen reichen nicht für Website-Login

**Vermutung:** Suno verwendet Clerk Auth mit serverseitiger Session-Validierung. Die Cookies allein reichen nicht - es wird eine aktive Session auf dem Server erwartet.

### Mögliche Lösungen

1. **Browser mit persistentem Profil** - Chrome/Firefox mit gespeichertem Login
2. **Clerk API direkt** - Token-Refresh über Clerk API
3. **Manuelle Generierung** - Tom generiert die 9 Tracks selbst (~10 Min)

### 19:49 - yt-dlp Versuch

**Entdeckung:** yt-dlp kann Suno-Seiten parsen!

```
yt-dlp -F "https://suno.com/s/CCgjkqMkRiQvYUVm"
→ Format gefunden: mp3, audio only
```

**Problem:** Download liefert nur ~0.1 Sekunden Fragment
- Echter Track: 269.64 Sekunden
- Heruntergeladen: 0.096 Sekunden (4.8KB)

**Ursache:** Suno schützt den echten Audio-Stream

### 19:53 - Finale Lösung ✅

**Manueller Download durch User:**
1. Track auf Suno öffnen
2. Drei-Punkte-Menü (⋮) → Download
3. MP3 an Aether senden
4. Integration ins Spiel

---

## Lessons Learned

1. **Clerk Auth ist komplex** — Cookies allein reichen nicht für Website-Login
2. **CDN ist geschützt** — Referer/Auth Header werden geprüft
3. **yt-dlp findet Metadaten** — aber Suno blockiert echte Audio-Downloads
4. **Manueller Download** — zuverlässigste Methode für jetzt

## Für die Zukunft

- [ ] Browser-Extension die Downloads automatisiert?
- [ ] Suno API wenn sie öffentlich wird?
- [ ] Alternative Musik-Generatoren mit offener API (Udio, etc.)?
- [ ] Persistent Browser Profile mit echtem Login?
