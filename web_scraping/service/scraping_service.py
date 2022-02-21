import urllib.request
from bs4 import BeautifulSoup

from web_scraping.module.mongo.mongoConnect import get_connection


def colhendo_dados(url: str):

    # especifique o URL
    # wiki = "https://www.zapimoveis.com.br/venda/imoveis/am+manaus/?gclid=Cj0KCQiA3rKQBhCNARIsACUEW_avk2vwJ3Zz2J6JhKpu6rNGC_Mdtv5ffGLZcBbKXwPQdqOHdEsbLb8aAlcQEALw_wcB&utm_referrer=https%3A%2F%2Fwww.google.com%2F&transacao=Venda&tipo=Im%C3%B3vel%20usado&onde=,Amazonas,Manaus,,,,,city,BR%3EAmazonas%3ENULL%3EManaus,-5.78417,-35.199971,%2Fvenda%2Fimoveis%2Fam%2Bmanaus%2F"

    # Consulte o site e retorne o html para a variável 'page'
    # page = urllib.request.urlopen(wiki)

    # Parse o html na variável 'page' e armazene-o no formato BeautifulSoup
    # soup = BeautifulSoup(page, 'html.parser')

    # print(soup.prettify())

    item_1 = {
        "_id": "U1IT00001",
        "item_name": "House 1",
        "adress": "69082-260",
        "price": 340,
        "category": "home"
    }

    collection_name = get_connection()['list_announcement']

    collection_name.insert_one(item_1)

    # # Insira a tag <li> e adicione sua classe
    # list_item = soup.find('li', attrs={'class': 'toclevel-2 tocsection-26'})
    #
    # name = list_item.text.strip()
    # print(name)
