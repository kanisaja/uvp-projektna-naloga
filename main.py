import time
from pobiranje_osnov import vzorci_na_n_straneh
from pobiranje_podrobnosti import podatki_vzorcev
from shranjevanje_v_csv import shrani_vzorce

start = time.time()
print('Začetek')
# pobere 3000 vzorcev
shrani_vzorce(podatki_vzorcev(vzorci_na_n_straneh(30)))
print('Konec')
print(time.time() - start)
