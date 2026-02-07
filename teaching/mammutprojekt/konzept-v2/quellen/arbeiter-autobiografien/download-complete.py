#!/usr/bin/env python3
"""Download complete worker autobiographies from Zeno.org"""
import urllib.request
import urllib.parse
import html
import re
import time
import os

def extract_text(html_content):
    """Extract main text content from Zeno.org HTML"""
    text = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL | re.IGNORECASE)
    
    match = re.search(r'<h5[^>]*>(.*?)</h5>\s*(.*?)<div[^>]*class="[^"]*footer', text, re.DOTALL | re.IGNORECASE)
    if not match:
        match = re.search(r'<h5[^>]*>(.*?)</h5>\s*(.*?)ZenoServer', text, re.DOTALL | re.IGNORECASE)
    
    if match:
        title = match.group(1)
        content = match.group(2)
    else:
        match = re.search(r'<body[^>]*>(.*?)</body>', text, re.DOTALL | re.IGNORECASE)
        content = match.group(1) if match else text
        title = ""
    
    content = re.sub(r'<br\s*/?>', '\n', content)
    content = re.sub(r'</p>', '\n\n', content)
    content = re.sub(r'<[^>]+>', '', content)
    content = html.unescape(content)
    content = re.sub(r'\n{3,}', '\n\n', content)
    content = re.sub(r'[ \t]+', ' ', content)
    content = '\n'.join(line.strip() for line in content.split('\n'))
    content = re.sub(r'(Bibliothek|Lesesaal|Kategorien|Shop|Nutzungsbedingungen|Datenschutzerklärung|Impressum|ZenoServer).*?(\n|$)', '', content)
    
    title = re.sub(r'<[^>]+>', '', title)
    title = html.unescape(title).strip()
    
    return title, content.strip()

def download_work(title, base_url, chapters, outfile, delay=1):
    """Download a complete work"""
    print(f"\n=== {title} ===")
    print(f"Chapters: {len(chapters)}")
    
    total_chars = 0
    with open(outfile, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n")
        f.write(f"# Quelle: Zeno.org (Public Domain)\n\n")
        
        for chapter in chapters:
            url = base_url + "/" + chapter
            print(f"  Downloading: {urllib.parse.unquote(chapter)[:40]}...")
            
            try:
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=30) as response:
                    content = response.read().decode('utf-8', errors='replace')
                
                ch_title, text = extract_text(content)
                if text and len(text) > 100:
                    f.write(f"\n## {ch_title}\n\n")
                    f.write(text)
                    f.write("\n\n---\n")
                    total_chars += len(text)
                    print(f"    ✓ {len(text)} chars")
                
                time.sleep(delay)
            except Exception as e:
                print(f"    ✗ {e}")
    
    with open(outfile, 'r') as f:
        lines = len(f.readlines())
    
    print(f"  Total: {lines} lines, {total_chars:,} chars")
    return lines, total_chars

if __name__ == "__main__":
    outdir = "/root/.openclaw/workspace/teaching/mammutprojekt/konzept-v2/quellen/arbeiter-autobiografien"
    os.makedirs(outdir, exist_ok=True)
    
    works = [
        {
            "title": "Franz Rehbein: Das Leben eines Landarbeiters (1911)",
            "base": "http://www.zeno.org/Kulturgeschichte/M/Rehbein,+Franz/Das+Leben+eines+Landarbeiters",
            "chapters": [
                "Aus+meinen+Kinderjahren",
                "Als+Hütejunge+beim+holsteinischen+Kleinbauern",
                "Als+Dienstjunge+in+der+Holsteinischen+»Grafenecke«",
                "Als+Dienstknecht+in+Dithmarschen",
                "Großknecht",
                "Ein+Stück+hinterpommerscher+Gutswirtschaft",
                "Im+Sachsengängerzuge",
                "Im+Tagelöhnerjoch",
                "Drei+Jahre+Kavallerist",
                "Schluss"
            ],
            "outfile": "rehbein-landarbeiter.txt"
        },
        {
            "title": "Ottilie Baader: Ein steiniger Weg - Lebenserinnerungen (1921)",
            "base": "http://www.zeno.org/Kulturgeschichte/M/Baader,+Ottilie/Ein+steiniger+Weg",
            "chapters": [
                "Vorwort",
                "Kindheit+und+Jugend",
                "Erste+Kämpfe",
                "In+der+Arbeiterbewegung",
                "Nachwort"
            ],
            "outfile": "baader-steiniger-weg.txt"
        },
        {
            "title": "Doris Viersbeck: Erlebnisse eines Hamburger Dienstmädchens (1910)",
            "base": "http://www.zeno.org/Kulturgeschichte/M/Viersbeck,+Doris/Erlebnisse+eines+Hamburger+Dienstmädchens",
            "chapters": [],  # Will be discovered
            "outfile": "viersbeck-dienstmaedchen.txt"
        },
        {
            "title": "Franz Bergg: Ein Proletarierleben (1913)",
            "base": "http://www.zeno.org/Kulturgeschichte/M/Bergg,+Franz/Ein+Proletarierleben",
            "chapters": [],
            "outfile": "bergg-proletarierleben.txt"
        }
    ]
    
    summary = []
    for work in works:
        # If chapters not specified, try to discover them
        if not work["chapters"]:
            print(f"\nDiscovering chapters for {work['title']}...")
            try:
                req = urllib.request.Request(work["base"], headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=30) as response:
                    content = response.read().decode('utf-8', errors='replace')
                
                # Find chapter links
                base_path = work["base"].replace("http://www.zeno.org", "")
                pattern = rf'href="({re.escape(base_path)}/[^"]+)"'
                matches = re.findall(pattern, content)
                work["chapters"] = [m.replace(base_path + "/", "") for m in matches]
                print(f"  Found {len(work['chapters'])} chapters")
            except Exception as e:
                print(f"  Error: {e}")
        
        if work["chapters"]:
            outfile = os.path.join(outdir, work["outfile"])
            lines, chars = download_work(work["title"], work["base"], work["chapters"], outfile)
            summary.append((work["title"], lines, chars))
        
        time.sleep(2)
    
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    for title, lines, chars in summary:
        print(f"{title}: {lines} lines, {chars:,} chars")
