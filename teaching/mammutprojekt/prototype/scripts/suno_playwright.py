#!/usr/bin/env python3
"""
Suno.ai Musik-Generierung via Playwright
Versuch: Browser-Automation mit Cookie-Injection
"""

import asyncio
import json
import os
from pathlib import Path
from datetime import datetime

# Logging
LOG_FILE = Path(__file__).parent / "SUNO_INTEGRATION.md"

def log(message: str):
    """Append to log file"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"\n**[{timestamp}]** {message}\n")
    print(f"[{timestamp}] {message}")

async def main():
    from playwright.async_api import async_playwright
    
    log("🚀 Starte Playwright Browser-Automation")
    
    # Cookie laden
    cookie_value = None
    env_path = Path.home() / ".openclaw/.env"
    with open(env_path) as f:
        for line in f:
            if line.startswith("SUNO_COOKIE="):
                cookie_value = line.strip().split("=", 1)[1]
                break
    
    if not cookie_value:
        log("❌ SUNO_COOKIE nicht in .env gefunden")
        return
    
    log(f"✅ Cookie geladen ({len(cookie_value)} Zeichen)")
    
    async with async_playwright() as p:
        # Browser starten (headless)
        log("📦 Starte Chromium (headless)...")
        
        try:
            browser = await p.chromium.launch(
                headless=True,
                args=['--no-sandbox', '--disable-dev-shm-usage']
            )
            log("✅ Browser gestartet")
        except Exception as e:
            log(f"❌ Browser-Start fehlgeschlagen: {e}")
            return
        
        # Neuer Context mit Cookies
        context = await browser.new_context(
            viewport={'width': 1280, 'height': 720},
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        )
        
        # Cookie setzen
        log("🍪 Setze Session-Cookie...")
        await context.add_cookies([
            {
                'name': '__session',
                'value': cookie_value,
                'domain': '.suno.com',
                'path': '/',
                'httpOnly': True,
                'secure': True,
                'sameSite': 'Lax'
            }
        ])
        log("✅ Cookie gesetzt")
        
        # Neue Seite
        page = await context.new_page()
        
        # Zu Suno navigieren
        log("🌐 Navigiere zu suno.com...")
        try:
            response = await page.goto('https://suno.com', wait_until='networkidle', timeout=30000)
            log(f"✅ Seite geladen (Status: {response.status})")
        except Exception as e:
            log(f"❌ Navigation fehlgeschlagen: {e}")
            await browser.close()
            return
        
        # Screenshot für Debug
        screenshot_path = Path(__file__).parent.parent / "debug_suno_home.png"
        await page.screenshot(path=str(screenshot_path))
        log(f"📸 Screenshot: {screenshot_path}")
        
        # Prüfen ob eingeloggt
        await asyncio.sleep(2)
        page_content = await page.content()
        
        if "Sign in" in page_content or "Log in" in page_content:
            log("❌ NICHT eingeloggt - Cookie wird nicht akzeptiert")
            log("   Mögliche Gründe:")
            log("   - Cookie abgelaufen")
            log("   - Falsches Cookie-Format")
            log("   - Suno erkennt Automation")
        elif "Create" in page_content:
            log("✅ Eingeloggt! 'Create' Button gefunden")
            
            # Zur Create-Seite navigieren
            log("🎵 Navigiere zur Create-Seite...")
            try:
                await page.goto('https://suno.com/create', wait_until='networkidle', timeout=30000)
                await asyncio.sleep(2)
                
                screenshot_path2 = Path(__file__).parent.parent / "debug_suno_create.png"
                await page.screenshot(path=str(screenshot_path2))
                log(f"📸 Screenshot: {screenshot_path2}")
                
                # Suche nach Input-Feld
                input_field = await page.query_selector('textarea[placeholder*="song"], textarea[placeholder*="describe"], input[type="text"]')
                if input_field:
                    log("✅ Input-Feld gefunden!")
                else:
                    log("⚠️ Input-Feld nicht gefunden - UI möglicherweise anders")
                    
            except Exception as e:
                log(f"❌ Create-Seite Fehler: {e}")
        else:
            log("⚠️ Unklarer Status - weder Login noch Create sichtbar")
        
        # Page-Title loggen
        title = await page.title()
        log(f"📄 Seiten-Titel: {title}")
        
        # Cleanup
        await browser.close()
        log("🏁 Browser geschlossen")

if __name__ == "__main__":
    asyncio.run(main())
