"""
fetch_huggingface.py

Fetches quirky AI projects from HuggingFace Spaces via API.
"""

import requests

def fetch_huggingface_projects():
    url = "https://huggingface.co/api/spaces?full=true&limit=20&sort=likes"
    response = requests.get(url)
    projects = []
    if response.status_code == 200:
        for space in response.json():
            projects.append({
                "title": space.get("id"),
                "url": f"https://huggingface.co/spaces/{space.get('id')}",
                "description": space.get("cardData", {}).get("description", "No description")
            })
    return projects
