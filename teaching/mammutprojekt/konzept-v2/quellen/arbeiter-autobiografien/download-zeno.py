#!/usr/bin/env python3
"""Download worker autobiographies from Zeno.org"""
import urllib.request
import urllib.parse
import html
import re
import time
import os

def extract_text(html_content):
    """Extract main text content from Zeno.org HTML"""
    # Remove scripts and styles
    text = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL | re.IGNORECASE)
    
    # Find main content - typically in the text between navigation elements
    # Look for the actual text after the title
    match = re.search(r'<h5[^>]*>(.*?)</h5>\s*(.*?)<div[^>]*class="[^"]*footer', text, re.DOTALL | re.IGNORECASE)
    if not match:
        match = re.search(r'<h5[^>]*>(.*?)</h5>\s*(.*?)ZenoServer', text, re.DOTALL | re.IGNORECASE)
    
    if match:
        title = match.group(1)
        content = match.group(2)
    else:
        # Fallback: extract everything between body tags
        match = re.search(r'<body[^>]*>(.*?)</body>', text, re.DOTALL | re.IGNORECASE)
        content = match.group(1) if match else text
        title = ""
    
    # Clean up HTML
    content = re.sub(r'<br\s*/?>', '\n', content)
    content = re.sub(r'</p>', '\n\n', content)
    content = re.sub(r'<[^>]+>', '', content)  # Remove all remaining tags
    content = html.unescape(content)
    
    # Clean up whitespace
    content = re.sub(r'\n{3,}', '\n\n', content)
    content = re.sub(r'[ \t]+', ' ', content)
    content = '\n'.join(line.strip() for line in content.split('\n'))
    
    # Remove navigation remnants
    content = re.sub(r'(Bibliothek|Lesesaal|Kategorien|Shop|Nutzungsbedingungen|Datenschutzerklärung|Impressum|ZenoServer).*?(\n|$)', '', content)
    
    title = re.sub(r'<[^>]+>', '', title)
    title = html.unescape(title).strip()
    
    return title, content.strip()

def download_chapter(url, delay=1):
    """Download a single chapter"""
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=30) as response:
            content = response.read().decode('utf-8', errors='replace')
        time.sleep(delay)
        return extract_text(content)
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return None, None

def download_bromme():
    """Download all Bromme chapters"""
    base = "http://www.zeno.org/Kulturgeschichte/M/Bromme,+Moritz+Theodor+William/Lebensgeschichte+eines+modernen+Fabrikarbeiters"
    
    chapters = [
        "Zur+Einleitung",
        "Meine+Großeltern",
        "Meine+Eltern", 
        "Meine+Kindheit+in+Schmölln",
        "In+den+Steinnußkopffabriken+Schmöllns",
        "Meine+Kellnerlaufbahn",
        "Pantoffelmacher",
        "In+Ronneburg,+den+neuen+Heimat",
        "Ein+Jahr+der+Unordnung",
        "Arbeitskollegen+und+Andere",
        "Verheiratet",
        "In+der+Gerarer+Werkzeug-+und+Maschinenfabrik+Wesselmann+Bohrer+&+Co.",
        "In+der+Lungenheilanstalt",
        "Mein+Familienleben"
    ]
    
    outdir = "/root/.openclaw/workspace/teaching/mammutprojekt/konzept-v2/quellen/arbeiter-autobiografien"
    outfile = os.path.join(outdir, "bromme-lebensgeschichte.txt")
    
    with open(outfile, 'w', encoding='utf-8') as f:
        f.write("# Moritz Bromme: Lebensgeschichte eines modernen Fabrikarbeiters (1905)\n")
        f.write("# Quelle: Zeno.org (Public Domain)\n")
        f.write("# Originalausgabe: Jena, Diederichs 1905\n\n")
        
        for chapter in chapters:
            url = f"{base}/{urllib.parse.quote(urllib.parse.unquote_plus(chapter), safe='+')}"
            print(f"Downloading: {urllib.parse.unquote_plus(chapter)}...")
            
            title, content = download_chapter(url)
            
            if content:
                f.write(f"\n## {title}\n\n")
                f.write(content)
                f.write("\n\n---\n")
                print(f"  ✓ {len(content)} chars")
            else:
                print(f"  ✗ Failed")
    
    # Count lines
    with open(outfile, 'r') as f:
        lines = len(f.readlines())
    print(f"\nDone! Saved {lines} lines to {outfile}")

if __name__ == "__main__":
    download_bromme()
