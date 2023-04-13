import requests
import time
from bs4 import BeautifulSoup
from tech_news.database import create_news

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


# Requisito 5
def get_tech_news(amount):
    first_page = fetch("https://blog.betrybe.com/")
    news_links = scrape_updates(first_page)
    next_link = scrape_next_page_link(first_page)
    while len(news_links) < amount:
        next_page = fetch(next_link)
        news_links.extend(scrape_updates(next_page))
        next_link = scrape_next_page_link(next_page)
    news = [scrape_news(fetch(link)) for link in news_links[:amount]]
    create_news(news)
    return news
