"""
fetch_and_score.py

Fetches new AI projects from Product Hunt RSS and scores them for quirkiness using GPT-3.5.
"""

import feedparser
import openai
import json
import os
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")
feed_url = "https://www.producthunt.com/feed"
feed = feedparser.parse(feed_url)

ai_projects = []
for entry in feed.entries:
    if "AI" in entry.title or "GPT" in entry.summary:
        ai_projects.append({
            "title": entry.title,
            "url": entry.link,
            "description": entry.summary
        })

def score_with_gpt(project):
    prompt = f"Rate how quirky and original this AI project is on a scale from 1 to 10. Quirky means unusual, playful, or unexpected.\n\nTitle: {project['title']}\nDescription: {project['description']}\n\nRespond with just the number."
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        score = int(response['choices'][0]['message']['content'].strip())
    except Exception:
        score = 5
    return min(max(score, 1), 10)

scored_projects = []
for p in ai_projects:
    scored_project = {
        "title": p["title"],
        "url": p["url"],
        "description": p["description"],
        "quirky_score": score_with_gpt(p),
        "tags": ["ai", "quirky"],
        "date_added": datetime.now().strftime("%Y-%m-%d")
    }
    scored_projects.append(scored_project)

with open("data/quirky_projects.json", "r") as f:
    existing = json.load(f)

existing_urls = {p["url"] for p in existing}
new_projects = [p for p in scored_projects if p["url"] not in existing_urls]

with open("data/quirky_projects.json", "w") as f:
    json.dump(existing + new_projects, f, indent=2)

print(f"Added {len(new_projects)} new quirky projects.")
