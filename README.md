# Projektna naloga - Analiza vzorcev za kvačkanje
*Avtor: Kanisaja Nika Kovačič*

To je projektna naloga za predmet Uvod v programiranje v šolskem letu 2024/2025. 

Cilj projektne naloge je bil zbrati podatke o 3000 vzorcih za kvačkanje s spletne strani [Lovecrafts](https://www.lovecrafts.com/en-gb/) in ugotoviti kateri parametri so povezani s ceno in priljubljenostjo vzorcev. Parametri ki sem jih zbrala in analizirala so vrsta izdelka, podjetje, avtor, jezik, število vzorcev, število strani in raven znanja. 

Naredila sem dve verziji analize. Prva je bolj podrobna analiza podatkov, zbranih 1. septembra, 2025. V drugi mapi je splošna analiza podatkov, zbranih na dan zadnjega zagona programa, ki uporabi enake funkcije kot podrobna analiza, vendar ne vsebuje mojih komentarjev.

## Navodila za uporabo

### Potrebno orodje
Za uporabo programa je potrebno imeti na računalniku nameščena programa [Python](https://www.python.org/downloads/) in [Git](https://git-scm.com/downloads).

### Nalaganje datotek in knjižnic
Za nalaganje potrebnih datotek odprite ukazno vrstico in se z ukazoma ```cd``` in ```dir``` orientirajte do mape, kamor jih želite namestiti. Nato v ukazno vrstico prekopirajte spodnji ukaz:
```
git clone https://github.com/kanisaja/uvp-projektna-naloga.git
```
Potrebno je naložiti tudi uporabljene knižnice, kar storite v ukazni vrstici s sledečim ukazom:
```
pip install -r requirements.txt
```

### Uporaba programa

Spet se z ukazoma ```cd``` in ```dir``` premaknite do mape, v kateri je sedaj shranjen repozitorij. Program zaženete z ukazom:
```
python glavna_datoteka.py
```
Nato sledite navodilom, ki se izpišejo v ukazni vrstici.
