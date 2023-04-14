from tech_news.database import search_news
from collections import Counter


# Requisito 10
def top_5_categories():
    all_news = search_news({})
    categories = Counter(news["category"] for news in all_news)
    # Esta ordenação em duas passadas só funciona porque o sorted()
    # é estável: não altera a ordem relativa dos elementos
    # comparados como iguais
    first_order = sorted(categories.items(), key=lambda item: item[0])
    second_order = sorted(first_order, key=lambda item: item[1], reverse=True)
    return [item[0] for item in second_order][:5]
