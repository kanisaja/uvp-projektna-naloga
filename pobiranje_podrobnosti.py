from concurrent.futures import ThreadPoolExecutor
from pobiranje_osnov import prosnja


def podatki_vzorca(vzorec):
    '''
    Prejme slovar z osnovnimi podatki vzorca in posodobi slovar s podrobnimi
    podatki(vrsta, podjetje, avtor, jezik, število vzorcev, število strani,
    raven znanja)
    '''
    povezava = vzorec['Link']
    juha = prosnja(povezava)

    vrsta_vzorca = juha.find_all('li', class_='sf-breadcrumbs__list-item')[3]
    vzorec['Type'] = vrsta_vzorca.text.strip()

    tabela = juha.find_all('div', class_='sf-property--without-suffix '
                           'sf-property--value-in-middle sf-property')
    for vrstica in tabela:
        podatek = vrstica.find('dt').text.strip()
        podatki = ['Brand', 'Designer', 'Format', 'Language',
                   'Number of patterns', 'Pages', 'Skill Level']
        if podatek not in podatki:
            continue

        vrednost = vrstica.find('dd').text.strip()
        vzorec[podatek] = vrednost


def podatki_vzorcev(seznam_vzorcev):
    '''
    Prejme seznam slovarjev vzorcev in vrne seznam posodobljenih slovarjev
    vzorcev s podrobnimi podatki (vrsta, podjetje, avtor, jezik, število
    vzorcev, število strani, raven znanja)
    '''
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(podatki_vzorca, seznam_vzorcev)
    return seznam_vzorcev
