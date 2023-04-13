import requests
import time
from bs4 import BeautifulSoup

HEADERS = {
    "user-agent": "Fake user-agent"
}


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=3)
        time.sleep(1)
        if response.status_code != 200:
            return None
        return response.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    soup = BeautifulSoup(
        html_content, "html.parser").find("div", {"class": "archive-main"})
    links = []
    if html_content != "":
        for post in soup.find_all("article"):
            links.append(post.find("h2", {"class": "entry-title"}).a["href"])
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
