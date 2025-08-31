import csv


def shrani_vzorce(seznam_vzorcev):
    '''Shrani seznam slovarjev vzorcev v datoteko vzorci.csv'''
    with open('vzorci.csv', 'w', encoding='utf-8') as dat:
        pisatelj = csv.writer(dat)

        pisatelj.writerow(
            ['Ime', 'Cena', 'Vrsta', 'Podjetje', 'Avtor', 'Jezik',
             'Število vzorcev', 'Število strani', 'Raven znanja']
        )
        for vzorec in seznam_vzorcev:
            pisatelj.writerow(
                [
                    vzorec.get('Name', ''),
                    vzorec.get('Price', ''),
                    vzorec.get('Type', ''),
                    vzorec.get('Brand', ''),
                    vzorec.get('Designer', ''),
                    vzorec.get('Language', ''),
                    vzorec.get('Number of patterns', ''),
                    vzorec.get('Pages', ''),
                    vzorec.get('Skill Level', '')

                ]
            )
