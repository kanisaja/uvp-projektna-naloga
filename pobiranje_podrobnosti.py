from pobiranje_osnov import prosnja


def podatki_vzorca(vzorec):
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
    for vzorec in seznam_vzorcev:
        podatki_vzorca(vzorec)
    return seznam_vzorcev
