# Funkcije v tej datoteki so urejene po poglavjih, kjer se pojavijo v
# analiza.ipynb

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# izgled grafov

sns.set_theme(style="whitegrid", palette="deep")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False,
                     "axes.spines.left": False, "axes.spines.bottom": False})

vzorci = pd.read_csv('vzorci.csv', sep=',')


# Manjkajoči podatki

def korelacija_manjkanja_in_nizje_(metrika, naslov, ustrezen_predznak=1):
    '''
    Izpiše graf, ki kaže korelacije med višjo količino določenega manjkajočega
    podatka in nižjo metriko vzorca, potrebno je vnesti še (dopolnitev) naslova
    grafa in neobvezno predznak: -1 (za to je odvisno kako so podatki
    razporejeni)
    '''
    for stolpec in vzorci.columns:
        if stolpec != metrika and vzorci[stolpec].count() != 3000:
            vzorci[f'{stolpec} manjka'] = vzorci[stolpec].isnull()

    korelacije = {}
    for stolpec in vzorci.columns:
        if 'manjka' in stolpec:

            korelacija = vzorci[metrika].corr(vzorci[stolpec])
            korelacije[stolpec] = korelacija * ustrezen_predznak

    korelacije_serija = pd.Series(korelacije)

    korelacije_serija.plot(kind='barh')
    plt.title(f'Korelacija med manjkajočimi podatki in nižjo {naslov}')
    plt.xlabel('Korelacija')
    plt.show()
    print(f'Korelacija z nižjo {naslov}:')
    for kljuc, vrednost in korelacije.items():
        print(f'\t- {kljuc}: {vrednost:.3f}')


# Povezava med ceno in priljubljenostjo

def korelacija_cena_priljubljenost():
    '''izpiše korelacijo med ceno in priljubljenostjo'''
    korelacija = vzorci['Priljubljenost'].corr(vzorci['Cena [£]'])
    print(f'Korelacija med ceno in priljubljenostjo: {- korelacija:.3f}')


def cena_priljubljenost():
    '''
    Prikaže graf cene glede na priljubljenost vzorca in izpiše korelacijo
    med tema dvema spremenljivkama
    '''
    vzorci.plot(kind='scatter', x='Priljubljenost', y='Cena [£]', s=10)
    plt.title('Cena glede na priljubljenost')
    plt.show()


def koliko_placljivih_po(n):
    '''
    Izpiše koliko je plačljivih vzorcev po določenem številu
    priljubljenosti
    '''
    st = (vzorci[vzorci['Priljubljenost'] > n]['Cena [£]'] > 0).sum()
    print(f'Za vzorce manj priljubljene kot {n} je {st} plačljivih vzorcev')


# Avtorji

def stevilo_vzorcev(avtorja):
    '''Sprejme ime avtorja in vrne število vzorcev, ki jih je objavil (ki
    spadajo med 3000 najbolj priljubljenih vzorcev)'''
    steje = vzorci['Avtor'].value_counts()
    return steje[avtorja]


def avtorji_top_vzorcev(top_n, cena_ali_priljubljenost, gor):
    '''
    Sprejme število najbolj priljubljenih/dragih vzorcev in vrne NumPy array,
    ki vsebuje avtorje, ki so napisali te vzorce, avtorji se ne podvojujejo in
    manjkajoče avtorje izloči
    '''
    top_vzorci = vzorci.sort_values(cena_ali_priljubljenost,
                                    ascending=gor).head(top_n)
    top_vzorci_avtorji = top_vzorci['Avtor'].dropna().unique()
    return top_vzorci_avtorji


def povprecja_napisanih_vzorcev(top_n_vzorcev, cena_ali_priljubljenost,
                                opis, gor=True):
    '''
    Sprejme število najbolj priljubljenih/dragih vzorcev in izpiše aritmetično
    sredino in mediano objavljenih vzorcev (ki spadajo med 3000 najbolj
    priljubljenih vzorcev) za vse avtorje in za avtorje najbolj priljubljenih
    vzorcev. Za najdražje vzorce se paramtere gor nastavi na False
    '''
    vsi_avtorji = vzorci['Avtor'].value_counts()
    print('Vsi avtorji')
    print(f'Aritmetična sredina: {vsi_avtorji.mean():.2f}')
    print(f'Mediana: {vsi_avtorji.median()}')

    stevila = vsi_avtorji[avtorji_top_vzorcev(top_n_vzorcev,
                                              cena_ali_priljubljenost, gor)]
    print(f'\nAvtorji najbolj {opis} vzorcev:')
    print(f'Aritmetična sredina: {stevila.mean():.2f}')
    print(f'Mediana: {stevila.median()}')


def stevilo_objavljenih_vzorcev(top_n_vzorcev, cena_ali_priljubljenost,
                                gor=True):
    '''
    Sprejme število najbolj priljubljenih/dragih vzorcev in izpiše število
    objavljenih vzorcev (ki spadajo med 3000 najbolj priljubljenih vzorcev).
     Za najdražje vzorce se paramtere gor nastavi na False
    '''
    top_vzorci_avtorji = avtorji_top_vzorcev(top_n_vzorcev,
                                             cena_ali_priljubljenost, gor)
    print('Avtor: število objavljenih vzorcev')
    for avtor in top_vzorci_avtorji:
        print(f'{avtor}: {stevilo_vzorcev(avtor)}')


def stevilo_del_avtorjev(n_avtorjev):
    '''Prikaže graf poljunega števila avtorjev, ki so napisali največ vzorcev,
    ki spadajo med 3000 najbolj priljubljenih in izpiše koliko je najvišje
    število'''
    avtorji = vzorci.groupby(['Avtor']).size()
    avtorji_po_delih = avtorji.sort_values(ascending=False)
    top_avtorji = avtorji_po_delih.head(n_avtorjev)
    top_avtorji.plot(kind='bar', figsize=(12, 5))
    plt.title(f'{n_avtorjev} avtorjev z največ objavljenimi vzorci')
    plt.ylabel('Število vzorcev')
    plt.xticks(rotation=45, ha='right')
    plt.show()
    najvec = avtorji_po_delih.head(1).values[0]
    print(f'Največ napisanih vzorcev s strani enega avtorja: {najvec}. To '
          f'predstavlja {(najvec / 3000 * 100):.2f}% vseh vzorcev')
