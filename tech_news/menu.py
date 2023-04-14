import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)

# Requisitos 11 e 12
menu = """
Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por categoria;
 4 - Listar top 5 categorias;
 5 - Sair."""


def analyzer_menu():
    option = input(menu)
    match option:
        case "0":
            get_tech_news(
                int(input("Digite quantas notícias serão buscadas:")))
        case "1":
            search_by_title(input("Digite o título:"))
        case "2":
            search_by_date(
                input("Digite a data no formato aaaa-mm-dd:"))
        case "3":
            search_by_category(input("Digite a categoria:"))
        case "4":
            top_5_categories()
        case "5":
            print("Encerrando script\n")
        case _:
            sys.stderr.write("Opção inválida\n")
