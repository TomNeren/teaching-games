#!/usr/bin/env python3
"""Download worker autobiographies from Zeno.org with proper URL encoding"""
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
    
    title = re.sub(r'<[^>]+>', '', title)
    title = html.unescape(title).strip()
    
    return title, content.strip()

def fetch_url(url, retries=2):
    """Fetch URL with proper encoding"""
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=30) as response:
                return response.read().decode('utf-8', errors='replace')
        except Exception as e:
            if attempt == retries - 1:
                raise e
            time.sleep(1)

def discover_chapters(base_url):
    """Discover all chapter URLs for a work"""
    content = fetch_url(base_url)
    
    # Extract all chapter links
    pattern = r'href="(/Kulturgeschichte/[^"]+)"'
    matches = re.findall(pattern, content)
    
    # Filter to only child pages of this work
    base_path = urllib.parse.urlparse(base_url).path
    chapters = []
    for m in matches:
        if m.startswith(base_path + "/") and m not in chapters:
            chapters.append(m)
    
    return chapters

def download_work(title, base_url, outfile, delay=1):
    """Download a complete work"""
    print(f"\n=== {title} ===")
    
    chapters = discover_chapters(base_url)
    print(f"Found {len(chapters)} chapters")
    
    if not chapters:
        print("  No chapters found!")
        return 0, 0
    
    total_chars = 0
    with open(outfile, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n")
        f.write(f"# Quelle: Zeno.org (Public Domain)\n\n")
        
        for chapter_path in chapters:
            url = "http://www.zeno.org" + chapter_path
            chapter_name = urllib.parse.unquote(chapter_path.split("/")[-1])
            print(f"  {chapter_name[:50]}...", end=" ", flush=True)
            
            try:
                content = fetch_url(url)
                ch_title, text = extract_text(content)
                
                if text and len(text) > 100:
                    f.write(f"\n## {ch_title}\n\n")
                    f.write(text)
                    f.write("\n\n---\n")
                    total_chars += len(text)
                    print(f"✓ {len(text):,} chars")
                else:
                    print("(skipped - too short)")
                
                time.sleep(delay)
            except Exception as e:
                print(f"✗ {e}")
    
    with open(outfile, 'r') as f:
        lines = len(f.readlines())
    
    print(f"  Total: {lines:,} lines, {total_chars:,} chars")
    return lines, total_chars

if __name__ == "__main__":
    outdir = "/root/.openclaw/workspace/teaching/mammutprojekt/konzept-v2/quellen/arbeiter-autobiografien"
    os.makedirs(outdir, exist_ok=True)
    
    works = [
        ("Franz Rehbein: Das Leben eines Landarbeiters (1911)",
         "http://www.zeno.org/Kulturgeschichte/M/Rehbein,+Franz/Das+Leben+eines+Landarbeiters",
         "rehbein-landarbeiter.txt"),
        
        ("Ottilie Baader: Ein steiniger Weg (1921)",
         "http://www.zeno.org/Kulturgeschichte/M/Baader,+Ottilie/Ein+steiniger+Weg",
         "baader-steiniger-weg.txt"),
        
        ("Doris Viersbeck: Erlebnisse eines Hamburger Dienstmädchens (1910)",
         "http://www.zeno.org/Kulturgeschichte/M/Viersbeck,+Doris/Erlebnisse+eines+Hamburger+Dienstm%C3%A4dchens",
         "viersbeck-dienstmaedchen.txt"),
        
        ("Ernst Schuchardt: Erinnerungen eines alten Webers",
         "http://www.zeno.org/Kulturgeschichte/M/Schuchardt,+Ernst",
         "schuchardt-weber.txt"),
    ]
    
    summary = []
    for title, url, filename in works:
        outfile = os.path.join(outdir, filename)
        try:
            lines, chars = download_work(title, url, outfile)
            summary.append((title, lines, chars))
        except Exception as e:
            print(f"Error: {e}")
            summary.append((title, 0, 0))
        time.sleep(2)
    
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    for title, lines, chars in summary:
        print(f"{title}: {lines:,} lines, {chars:,} chars")
