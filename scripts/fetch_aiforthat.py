"""
fetch_aiforthat.py

Scrapes recent AI tools from theresanaiforthat.com
"""

import requests
from bs4 import BeautifulSoup

def fetch_aiforthat_projects():
    url = "https://theresanaiforthat.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    cards = soup.select(".tool-card")
    projects = []
    for card in cards[:15]:
        title = card.select_one("h3").text.strip()
        desc = card.select_one("p").text.strip()
        link = url + card.select_one("a")["href"]
        projects.append({
            "title": title,
            "url": link,
            "description": desc
        })
    return projects
