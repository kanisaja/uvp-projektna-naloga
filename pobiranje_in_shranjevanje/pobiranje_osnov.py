import requests
from bs4 import BeautifulSoup


def prosnja(url):
    '''
    Pošlje .get zahtevo na podani url (str) in vrne BeautifulSoup objekt html
    vsebine.
    '''
    html = requests.get(url).text
    juha = BeautifulSoup(html, 'html.parser')
    return juha


def vzorci_na_eni_strani(url):
    '''
    Pridobi osnovne podatke (ime, cena, povezava do strani vzorca) o
    vseh vzorcih na poljubni strani url (str).
    '''
    juha = prosnja(url)
    html_vzorcev = juha.find_all('div', class_='lc-product-card')

    vzorci = []
    for html_vzorca in html_vzorcev:
        ime = html_vzorca.find('div',
                               class_='lc-product-card__title').text.strip()
        cena = html_vzorca.find('span', class_='lc-price__regular')
        if cena is None:
            cena = '£0.00'
        else:
            cena = cena.text.strip()
        povezava = html_vzorca.find('a').get('href')

        vzorec = {
            'Name': ime,
            'Price': cena,
            'Link': povezava
        }
        vzorci.append(vzorec)
    return vzorci


def vzorci_na_n_straneh(n):
    '''
    Pridobi osnovne podatke (ime, cena, povezava do dodatnih podatkov) o
    vseh vzorcih na prvih n (int) straneh.
    '''
    vzorci = []
    prva_stran = 'https://www.lovecrafts.com/en-gb/l/crochet?' \
                 'filter-type.en-GB=Patterns&itemsPerPage=100'
    vzorci += vzorci_na_eni_strani(prva_stran)
    for i in range(2, n + 1):
        naslednja_stran = prva_stran + '&page=' + str(i)
        vzorci += vzorci_na_eni_strani(naslednja_stran)
    return vzorci
