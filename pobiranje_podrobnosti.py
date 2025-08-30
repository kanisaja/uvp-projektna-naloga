from pobiranje_osnov import prosnja


def podatki_vzorca(vzorec):
    povezava = vzorec['Link']
    juha = prosnja(povezava)
    tabela = juha.find_all('div', class_='sf-property--without-suffix '
                           'sf-property--value-in-middle sf-property')
    for vrstica in tabela:
        naslov = vrstica.find('dt').text.strip()

        # izključimo stvari, ki nas ne zanimajo
        if naslov == 'Craft' or naslov == 'Notes' or \
           naslov == 'Featured product':
            continue

        vrednost = vrstica.find('dd').text.strip()
        vzorec[naslov] = vrednost
    return vzorec
