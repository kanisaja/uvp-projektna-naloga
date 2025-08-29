import requests
from bs4 import BeautifulSoup

glavna_povezava = 'https://www.lovecrafts.com/en-gb/l/crochet?\
    filter-type.en-GB=Patterns&itemsPerPage=100'


def vzorci_na_eni_strani(url):
    html = requests.get(url).text
    juha = BeautifulSoup(html, 'html.parser')
    html_vzorcev = juha.find_all('div', class_="lc-product-card")

    vzorci = []
    for _ in html_vzorcev:
        ime = _.find('div', class_="lc-product-card__title").text.strip()
        cena = _.find('span', class_="lc-price__regular")
        if cena is None:
            cena = '£0.00'
        else:
            cena = cena.text.strip()
        povezava = _.find('a').get('href')

        ime = {
            'cena': cena,
            'povezava': povezava
        }
        vzorci.append(ime)
    return vzorci
