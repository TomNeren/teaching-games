# TOOLS.md - Local Notes

Skills define *how* tools work. This file is for *your* specifics — the stuff that's unique to your setup.

---

## Websuche

| Tool | Befehl | Stärke |
|------|--------|--------|
| **Brave** | `web_search` (native) | Schnell, strukturiert |
| **DuckDuckGo** | `/root/.openclaw/tools/ddg "query"` | Kostenlos, unbegrenzt |
| **Tavily** | `mcporter call tavily.tavily_search query="..."` | Deep Research, Crawling |
| **Serper** | `mcporter call serper.google_search q="..." gl=de hl=de` | Google-Ergebnisse |

## Akademische Recherche

```bash
# Alle Quellen durchsuchen
/root/.openclaw/tools/research "pedagogy bilingual" -n 5

# Nur OpenAlex (260M+ Papers)
/root/.openclaw/tools/research "query" -s openalex --education

# Nur ERIC (US Education)
/root/.openclaw/tools/research "query" -s eric

# Fachportal Pädagogik
/root/.openclaw/tools/research "query" -s fachportal
```

**Quellen:**
- **OpenAlex** — 260M+ akademische Werke, Open Access, kostenlos
- **ERIC** — US Department of Education, Bildungsforschung
- **Fachportal Pädagogik** — Deutsche Bildungsforschung (DIPF)

---

## Email

- `gog` CLI installiert (v0.9.0)
- GCP-Projekt noch nicht eingerichtet

---

## Sonstiges

*Hier kommen lokale Notizen hin: Kamera-Namen, SSH-Hosts, TTS-Stimmen...*
