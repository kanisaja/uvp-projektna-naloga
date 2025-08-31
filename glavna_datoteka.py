import time
from pobiranje_in_shranjevanje import (vzorci_na_n_straneh, podatki_vzorcev,
                                       shrani_vzorce)

start = time.time()


def glavna_funkcija(n):
    '''
    Sprejme število n in pobere in shrani 100 * n vzorcev v datoteko
    vzorci.csv ter poda navodila za pogled analize podatkov
    '''
    print('Program zdaj pobira podatke s spletne strani. '
          'Prosim počakajte, da se pobiranje podatkov zaključi in nato '
          'sledite navodilom v terminalu.')

    vzorci = vzorci_na_n_straneh(n)
    podrobni_vzorci = podatki_vzorcev(vzorci)
    shrani_vzorce(podrobni_vzorci)

    minute = ((time.time() - start) // 60)
    sekunde = ((time.time() - start) % 60)
    sklanjatev = ''
    if sekunde == 1:
        sklanjatev = 'o'
    elif sekunde == 2:
        sklanjatev = 'i'
    elif sekunde in [3, 4]:
        sklanjatev = 'e'

    print('\nProgram je zaključil s pobiranjem podatkov. '
          f'Pobiranje je trajalo {minute:.0f} minut in '
          f'{sekunde:.0f} sekund{sklanjatev}.')
    print('Če želite pogledati analizo podatkov, v terminal napišite: '
          'jupyter notebook \n')


glavna_funkcija(30)
