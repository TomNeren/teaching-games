#!/usr/bin/env python3
"""Download multiple worker autobiographies from Zeno.org"""
import urllib.request
import urllib.parse
import html
import re
import time
import os
import sys

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

def get_chapters(author_url):
    """Get list of chapter URLs for an author"""
    try:
        req = urllib.request.Request(author_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=30) as response:
            content = response.read().decode('utf-8', errors='replace')
        
        # Find all chapter links
        pattern = rf'href="({re.escape(author_url.replace("http://www.zeno.org", ""))}[^"]+)"'
        matches = re.findall(pattern, content)
        
        # Also try to find work-specific links
        base_path = author_url.replace("http://www.zeno.org", "")
        pattern2 = rf'href="({base_path}/[^"]+)"'
        matches2 = re.findall(pattern2, content)
        
        all_matches = list(set(matches + matches2))
        return ["http://www.zeno.org" + m for m in all_matches if m != base_path]
    except Exception as e:
        print(f"Error getting chapters: {e}")
        return []

def download_author(author_name, author_url, outfile, delay=1):
    """Download all works by an author"""
    print(f"\n=== Downloading: {author_name} ===")
    
    chapters = get_chapters(author_url)
    if not chapters:
        # Try direct download of main page
        chapters = [author_url]
    
    print(f"Found {len(chapters)} chapter(s)")
    
    total_chars = 0
    with open(outfile, 'w', encoding='utf-8') as f:
        f.write(f"# {author_name}\n")
        f.write(f"# Quelle: Zeno.org (Public Domain)\n\n")
        
        for url in sorted(chapters):
            try:
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=30) as response:
                    content = response.read().decode('utf-8', errors='replace')
                
                title, text = extract_text(content)
                if text and len(text) > 100:
                    f.write(f"\n## {title}\n\n")
                    f.write(text)
                    f.write("\n\n---\n")
                    total_chars += len(text)
                    print(f"  ✓ {title[:50]}... ({len(text)} chars)")
                
                time.sleep(delay)
            except Exception as e:
                print(f"  ✗ {url}: {e}")
    
    with open(outfile, 'r') as f:
        lines = len(f.readlines())
    
    print(f"  Total: {lines} lines, {total_chars} chars")
    return lines

if __name__ == "__main__":
    outdir = "/root/.openclaw/workspace/teaching/mammutprojekt/konzept-v2/quellen/arbeiter-autobiografien"
    os.makedirs(outdir, exist_ok=True)
    
    # Authors to download (from "The German Worker" anthology)
    authors = [
        ("Franz Rehbein - Das Leben eines Landarbeiters", 
         "http://www.zeno.org/Kulturgeschichte/M/Rehbein,+Franz",
         "rehbein-landarbeiter.txt"),
        
        ("Ottilie Baader - Lebenserinnerungen", 
         "http://www.zeno.org/Kulturgeschichte/M/Baader,+Ottilie",
         "baader-lebenserinnerungen.txt"),
        
        ("Doris Viersbeck - Erlebnisse eines Hamburger Dienstmädchens",
         "http://www.zeno.org/Kulturgeschichte/M/Viersbeck,+Doris",
         "viersbeck-dienstmaedchen.txt"),
        
        ("Ernst Schuchardt - Erfahrungen eines alten Webers",
         "http://www.zeno.org/Kulturgeschichte/M/Schuchardt,+Ernst",
         "schuchardt-weber.txt"),
        
        ("Franz Bergg - Ein Proletarierleben",
         "http://www.zeno.org/Kulturgeschichte/M/Bergg,+Franz",
         "bergg-proletarierleben.txt"),
    ]
    
    for name, url, filename in authors:
        outfile = os.path.join(outdir, filename)
        try:
            download_author(name, url, outfile)
        except Exception as e:
            print(f"Error with {name}: {e}")
        time.sleep(2)
    
    print("\n=== Done! ===")
