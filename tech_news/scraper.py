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
    soup = BeautifulSoup(html_content, "html.parser")
    try:
        return soup.find(
            "a",
            {"class": "next page-numbers"},
        )["href"]
    except TypeError:
        return None


# Requisito 4
def scrape_news(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    link = soup.head.find("link", {"rel": "canonical"})["href"]
    title = soup.find("h1", {"class": "entry-title"}).string.strip()
    post_meta = soup.find("ul", {"class": "post-meta"})
    timestamp = post_meta.find("li", {"class": "meta-date"}).string
    writer = post_meta.find(
        "li", {"class": "meta-author"}
        ).find("span", {"class": "author"}).a.string
    reading_time_txt = post_meta.find(
        "li", {"class": "meta-reading-time"}
        ).contents[1]
    reading_time = "".join(char for char in reading_time_txt if char.isdigit())
    summary = soup.find("div", {"class": "entry-content"}).p.text.strip()
    category = soup.find(
        "div", {"class": "meta-category"}
        ).find("span", {"class": "label"}).string
    return {
        "url": link,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": int(reading_time),
        "summary": summary,
        "category": category,
    }


# print(scrape_news(fetch("https://blog.betrybe.com/tecnologia/cabos-de-rede/")))


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
