"""
fetch_nitter.py

Fetches quirky AI projects from Twitter via Nitter RSS proxy.
"""

import feedparser

def fetch_nitter_projects():
    feed = feedparser.parse("https://nitter.net/search/rss?f=tweets&q=%23AI+OR+%23GPT+OR+%23weirdAI")
    projects = []
    for entry in feed.entries[:15]:
        projects.append({
            "title": entry.title,
            "url": entry.link,
            "description": entry.summary
        })
    return projects
