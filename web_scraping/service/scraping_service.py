import urllib.request
import json
from bs4 import BeautifulSoup

from web_scraping.module.mongo.mongoConnect import get_connection


def colhendo_dados():
    # especifique o URL
    url = "https://am.olx.com.br/regiao-de-manaus/manaus/cidade-nova/imoveis/venda/apartamentos"

    # Consulte o site e retorne o html para a variável 'page'
    request = urllib.request.Request(url, headers={'user-agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'})
    page = urllib.request.urlopen(request)

    # Parse o html na variável 'page' e armazene-o no formato BeautifulSoup
    soup = BeautifulSoup(page, 'html.parser')

    # Busque pela tag <ul> que contem a lista de anuncios
    ads_list = soup.find('ul', {'id': 'ad-list'}).findAll('a')

    all_ads_data = []
    for ad in ads_list:
        all_ads_data.append(colhendo_dados_anuncio(ad['href']))

    collection_name = get_connection()['list_announcement']

    collection_name.insert_many(all_ads_data)


def colhendo_dados_anuncio(url):
    request = urllib.request.Request(url, headers={'user-agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'})
    page = urllib.request.urlopen(request)
    soup = BeautifulSoup(page, "html.parser")

    json_data = json.loads(soup.find('script', {'id': 'initial-data'})['data-json'])['ad']

    final_ad = {
        'id': json_data['listId'],
        'title': json_data['subject'],
        'description': json_data['body'],
        'price': json_data['priceValue'],
        'location': {
            'address': json_data['location']['address'],
            'neighbourhood': json_data['location']['neighbourhood'],
            'municipality': json_data['location']['municipality'],
            'zipcode': json_data['location']['zipcode'],
            'uf': json_data['location']['uf']
        },
        'properties': [{prop['label']: prop["value"]} for prop in json_data['properties']]
    }

    return final_ad
