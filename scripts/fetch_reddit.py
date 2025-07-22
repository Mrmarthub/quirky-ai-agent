"""
fetch_reddit.py

Fetches quirky AI projects from Reddit using praw.
"""

import praw

def fetch_reddit_projects():
    reddit = praw.Reddit(
        client_id="your_client_id",
        client_secret="your_client_secret",
        user_agent="quirky_ai_agent"
    )

    subreddit = reddit.subreddit("ChatGPT+ArtificialInteligence+SideProject")
    posts = subreddit.hot(limit=20)

    projects = []
    for post in posts:
        if "AI" in post.title or "GPT" in post.title:
            projects.append({
                "title": post.title,
                "url": post.url,
                "description": post.selftext or "No description"
            })
    return projects
