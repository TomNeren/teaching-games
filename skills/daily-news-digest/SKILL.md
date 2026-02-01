---
name: daily-news-digest
description: Daily news summary at 18:00 UTC covering Germany, Europe, USA, Paraguay, Africa, China, and Southeast Asia. Tracks seen news to avoid duplicates. Supports marking articles as "interesting" for weekly follow-up updates. Use for scheduled news briefings and news tracking.
---

# Daily News Digest

Provides curated daily news summaries with deduplication and follow-up tracking.

## Data Files (workspace)

Store in `news-data/`:
- `seen_news.md` - Hashes/titles of delivered news (prevents duplicates)
- `watchlist.md` - Articles marked interesting (weekly follow-up)

## Daily Summary (18:00 UTC)

1. Search news for each region using `web_search` with `freshness: "pd"` (past 24h)
2. Check each headline against `seen_news.md` - skip if already shown
3. Format summary by region with bullet points
4. Append new headlines to `seen_news.md` with date
5. Deliver to user

### Regions & Search Queries

| Region | Query |
|--------|-------|
| Germany | `Germany news today wichtige Nachrichten` |
| Europe | `Europe EU news today` |
| USA | `United States news today politics economy` |
| Paraguay | `Paraguay news today noticias` |
| Africa | `Africa news today` |
| China | `China news today` |
| Southeast Asia | `Southeast Asia news Vietnam Thailand Indonesia` |

## Marking Interesting

When user says an article is interesting:
1. Add to `watchlist.md` with: title, URL, date added, keywords
2. Confirm addition

## Weekly Watchlist Update (Sundays)

1. Read `watchlist.md`
2. For each item, search for updates using title/keywords
3. Report any new developments
4. Keep items on watchlist unless user removes them

## seen_news.md Format

```markdown
## 2026-02-01
- [hash] Germany: Headline here
- [hash] USA: Another headline

## 2026-01-31
- [hash] China: Old headline
```

Use first 8 chars of MD5 hash of headline for dedup.

## watchlist.md Format

```markdown
## Active

### Article Title
- URL: https://...
- Added: 2026-02-01
- Keywords: keyword1, keyword2
- Last checked: 2026-02-01

## Archived
(moved here when user removes)
```

## Cleanup

Monthly: Remove entries older than 30 days from `seen_news.md` to save space.
