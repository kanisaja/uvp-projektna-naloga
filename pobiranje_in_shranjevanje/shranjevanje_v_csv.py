import csv


def shrani_vzorce(seznam_vzorcev):
    '''Shrani seznam slovarjev vzorcev v datoteko vzorci.csv'''
    with open('splosna_analiza/vzorci.csv', 'w', encoding='utf-8') as dat:
        pisatelj = csv.writer(dat)

        pisatelj.writerow(
            ['Ime', 'Priljubljenost', 'Cena [£]', 'Vrsta izdelka', 'Podjetje',
             'Avtor', 'Jezik', 'Število vzorcev', 'Število strani',
             'Raven znanja']
        )
        priljubljenost = 1
        for vzorec in seznam_vzorcev:
            pisatelj.writerow(
                [
                    vzorec.get('Name', ''),
                    priljubljenost,
                    vzorec.get('Price', '').replace('£', ''),
                    vzorec.get('Type', ''),
                    vzorec.get('Brand', ''),
                    vzorec.get('Designer', ''),
                    vzorec.get('Language', '').replace(',', '|').replace(' ',
                                                                         ''),
                    vzorec.get('Number of patterns', ''),
                    vzorec.get('Pages', ''),
                    vzorec.get('Skill Level', '')

                ]
            )
            priljubljenost += 1
