import time
from pobiranje_osnov import vzorci_na_n_straneh
from pobiranje_podrobnosti import podatki_vzorcev
from shranjevanje_v_csv import shrani_vzorce

start = time.time()

# pobere 1000 vzorcev
shrani_vzorce(podatki_vzorcev(vzorci_na_n_straneh(10)))

print(time.time() - start)
