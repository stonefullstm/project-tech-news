from tech_news.database import search_news
import datetime


# Requisito 7
def search_by_title(title):
    result = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(news["title"], news["url"]) for news in result]


# Requisito 8
def search_by_date(date):
    try:
        # date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        fdate = datetime.datetime.fromisoformat(date).strftime("%d/%m/%Y")
        result = search_news({"timestamp": fdate})
    except ValueError:
        raise ValueError("Data inválida")
    else:
        return [(news["title"], news["url"]) for news in result]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
