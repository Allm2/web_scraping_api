# importe a biblioteca usada para consultar uma URL
import urllib.request

# importe as funções BeautifulSoup para analisar os dados retornados do site
from bs4 import BeautifulSoup


def colhendo_dados():
    # especifique o URL
    wiki = "https://pt.wikipedia.org/wiki/Lista_de_capitais_do_Brasil"

    # Consulte o site e retorne o html para a variável 'page'
    page = urllib.request.urlopen(wiki)

    # Parse o html na variável 'page' e armazene-o no formato BeautifulSoup
    soup = BeautifulSoup(page, 'html5lib')

    # Insira a tag <li> e adicione sua classe
    list_item = soup.find('li', attrs={'class': 'toclevel-2 tocsection-26'})

    name = list_item.text.strip()
    print(name)
