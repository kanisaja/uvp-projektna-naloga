# Funkcije v tej datoteki so urejene po poglavjih, kjer se pojavijo v
# analiza.ipynb

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# izgled grafov

sns.set_theme(style="whitegrid", palette="deep")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False,
                     "axes.spines.left": False, "axes.spines.bottom": False})


# Priprava na analizo

vzorci = pd.read_csv('vzorci.csv', sep=',')


def precisti_vrste_izdelkov():
    for indeks, ime, vrsta in vzorci[['Ime', 'Vrsta izdelka']].itertuples():
        if ime == vrsta:
            vzorci.loc[indeks, 'Vrsta izdelka'] = pd.NA


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
    plt.gca().invert_xaxis()
    plt.title('Cena glede na priljubljenost')
    plt.show()


def koliko_placljivih_po(n):
    '''
    Izpiše koliko je plačljivih vzorcev po določenem številu
    priljubljenosti
    '''
    st = (vzorci[vzorci['Priljubljenost'] > n]['Cena [£]'] > 0).sum()
    print(f'Za vzorce manj priljubljene kot {n} je {st} plačljivih vzorcev')


def koliko_placljivih_vzorcev():
    st = (vzorci['Cena [£]'] > 0).sum()
    print(f'Plačljivih vzorcev je: {st}')


# Avtorji

def stevilo_vzorcev(avtorja):
    '''Sprejme ime avtorja in vrne število vzorcev, ki jih je objavil (ki
    spadajo med 3000 najbolj priljubljenih vzorcev)'''
    steje = vzorci['Avtor'].value_counts()
    return steje[avtorja]


def avtorji_top_vzorcev(top_n, cena_ali_priljubljenost, asc):
    '''
    Sprejme število najbolj priljubljenih/dragih vzorcev in vrne NumPy array,
    ki vsebuje avtorje, ki so napisali te vzorce, avtorji se ne podvojujejo in
    manjkajoče avtorje izloči
    '''
    top_vzorci = vzorci.sort_values(cena_ali_priljubljenost,
                                    ascending=asc).head(top_n)
    top_vzorci_avtorji = top_vzorci['Avtor'].dropna().unique()
    return top_vzorci_avtorji


def povprecja_napisanih_vzorcev(top_n_vzorcev, cena_ali_priljubljenost,
                                opis, asc=True):
    '''
    Sprejme število najbolj priljubljenih/dragih vzorcev in izpiše aritmetično
    sredino in mediano objavljenih vzorcev (ki spadajo med 3000 najbolj
    priljubljenih vzorcev) za vse avtorje in za avtorje najbolj priljubljenih
    vzorcev. Za najdražje vzorce se paramtere asc nastavi na False
    '''
    vsi_avtorji = vzorci['Avtor'].value_counts()
    print('Vsi avtorji')
    print(f'Aritmetična sredina: {vsi_avtorji.mean():.2f}')
    print(f'Mediana: {vsi_avtorji.median()}')

    stevila = vsi_avtorji[avtorji_top_vzorcev(top_n_vzorcev,
                                              cena_ali_priljubljenost, asc)]
    print(f'\nAvtorji najbolj {opis} vzorcev:')
    print(f'Aritmetična sredina: {stevila.mean():.2f}')
    print(f'Mediana: {stevila.median()}')


def stevilo_objavljenih_vzorcev(top_n_vzorcev, cena_ali_priljubljenost,
                                asc=True):
    '''
    Sprejme število najbolj priljubljenih/dragih vzorcev in izpiše število
    objavljenih vzorcev (ki spadajo med 3000 najbolj priljubljenih vzorcev).
     Za najdražje vzorce se paramtere asc nastavi na False
    '''
    top_vzorci_avtorji = avtorji_top_vzorcev(top_n_vzorcev,
                                             cena_ali_priljubljenost, asc)
    print('Avtor: število objavljenih vzorcev')
    for avtor in top_vzorci_avtorji:
        print(f'{avtor}: {stevilo_vzorcev(avtor)}')


def stevilo_del_avtorjev(n_avtorjev):
    '''Prikaže graf poljunega števila avtorjev, ki so napisali največ vzorcev,
    ki spadajo med 3000 najbolj priljubljenih in izpiše koliko je najvišje
    število'''
    avtorji = vzorci.groupby('Avtor').size()
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


# Potrebna raven znanja in Vrsta izdelka

def stevec(kategorija):
    print(vzorci[kategorija].value_counts())


def primerjava(ravni_ali_vrste, cena_ali_priljubljenost):
    ravni = ['Beginner', 'Advanced Beginner', 'Intermediate', 'Advanced']
    vrste = (vzorci.groupby('Vrsta izdelka', observed='True')
             .size()
             .sort_values(ascending=False)
             .loc[lambda s: s > 50]
             .index
             .tolist())
    if ravni_ali_vrste == 'Raven znanja':
        izbrane = ravni
    else:
        izbrane = vrste
    vzorci[ravni_ali_vrste] = pd.Categorical(vzorci[ravni_ali_vrste],
                                             categories=izbrane, ordered=True)

    med = (vzorci.groupby(ravni_ali_vrste, observed=True)
           [cena_ali_priljubljenost].median())
    mean = (vzorci.groupby(ravni_ali_vrste, observed=True)
            [cena_ali_priljubljenost].mean())

    med.plot(label='mediana', marker='o')
    mean.plot(label='aritmetična sredina', marker='o')
    if cena_ali_priljubljenost == 'Priljubljenost':
        plt.gca().invert_yaxis()
    plt.title(f'{cena_ali_priljubljenost} v odvisnosti od '
              f'{ravni_ali_vrste.lower()}')
    plt.ylabel(cena_ali_priljubljenost)
    plt.xlabel(ravni_ali_vrste)
    plt.legend()
    plt.show()


# Jeziki

def priprava_jezikov():
    kopija = vzorci.copy()
    kopija['Jezik'] = vzorci['Jezik'].str.split('|')
    return kopija.explode('Jezik')


def stevec_jezikov():
    print(priprava_jezikov()['Jezik'].value_counts())


def jezik_in(cena_ali_priljubljenost):
    vzorci_exploded = priprava_jezikov()
    jeziki = (vzorci_exploded.groupby('Jezik', observed='True')
              .size()
              .sort_values(ascending=False)
              .loc[lambda s: s > 50]
              .index
              .tolist())
    vzorci_exploded['Jezik'] = pd.Categorical(vzorci_exploded['Jezik'],
                                              categories=jeziki, ordered=True)

    med = (vzorci_exploded.groupby('Jezik', observed=True)
           [cena_ali_priljubljenost].median())
    mean = (vzorci_exploded.groupby('Jezik', observed=True)
            [cena_ali_priljubljenost].mean())

    med.plot(label='mediana', marker='o')
    mean.plot(label='aritmetična sredina', marker='o')
    if cena_ali_priljubljenost == 'Priljubljenost':
        plt.gca().invert_yaxis()
    plt.title(f'{cena_ali_priljubljenost} v odvisnosti od jezika')
    plt.ylabel(cena_ali_priljubljenost)
    plt.xlabel('Jezik')
    plt.legend()
    plt.show()


# Podjetja

def priprava_podjetij_ali_st(podjetja_ali_st):
    kopija = vzorci.copy()
    if podjetja_ali_st == 'Podjetje':
        nov_stolpec = 'Tip avtorja'
        moznost_1 = 'Neodvisni avtor'
        moznost_2 = 'Podjetje'
        pogoj = 'Independent Designer'
    else:
        nov_stolpec = 'Tip po številu'
        moznost_1 = 'Posamezni vzorec'
        moznost_2 = 'Zbirka vzorcev'
        pogoj = 1
    kopija[nov_stolpec] = kopija[podjetja_ali_st].apply(
        lambda x: moznost_1 if x == pogoj
        else moznost_2
    )
    return kopija


def delez(podjetja_ali_st):
    if podjetja_ali_st == 'Podjetje':
        nov_stolpec = 'Tip avtorja'
        naslov = 'avtorjev'
    else:
        nov_stolpec = 'Tip po številu'
        naslov = 'izdelka glede na to kolikšno število vzorcev vključuje'
    kopija = priprava_podjetij_ali_st(podjetja_ali_st)
    delez = kopija[nov_stolpec].value_counts()
    delez.plot(kind='pie', autopct='%1.1f%%', shadow=True)
    plt.ylabel('')
    plt.title(f'Delež tipa {naslov}')
    plt.show()


def posamezni_proti_zbirki(podjetja_ali_st, cena_ali_priljubljenost):
    kopija = priprava_podjetij_ali_st(podjetja_ali_st)
    if podjetja_ali_st == 'Podjetje':
        nov_stolpec = 'Tip avtorja'
        naslov = 'tip avtorja'
        moznost_1 = 'Neodvisni avtor'
        moznost_2 = 'Podjetje'
    else:
        nov_stolpec = 'Tip po številu'
        naslov = 'število vzorcev v izdelku'
        moznost_1 = 'Posamezni vzorec'
        moznost_2 = 'Zbirka vzorcev'   

    med = (kopija.groupby(nov_stolpec)
           [cena_ali_priljubljenost].median())
    mean = (kopija.groupby(nov_stolpec)
            [cena_ali_priljubljenost].mean())

    med.plot(label='mediana', marker='o')
    mean.plot(label='aritmetična sredina', marker='o')
    if cena_ali_priljubljenost == 'Priljubljenost':
        plt.gca().invert_yaxis()
    plt.title(f'{cena_ali_priljubljenost} glede na {naslov}')
    plt.xlabel(nov_stolpec)
    plt.ylabel(cena_ali_priljubljenost)
    plt.xticks(np.arange(2), [moznost_1, moznost_2])
    plt.legend()
    plt.show()


def povprecje_napisanih_vzorcec_podjetij():
    samo_podjetja = vzorci[vzorci['Podjetje'] != 'Independent Designer']
    st_vzorcev_podjetij = samo_podjetja['Podjetje'].value_counts()
    print('Podjetja:')
    print(f'Aritmetična sredina: {st_vzorcev_podjetij.mean():.2f}')
    print(f'Mediana: {st_vzorcev_podjetij.median()}')

    neodvisni_avtorji = vzorci[vzorci['Podjetje'] == 'Independent Designer']
    st_vzorcev_neodvisnih_avtorjev = neodvisni_avtorji['Avtor'].value_counts()
    print('\nNeodvisni avtorji')
    print(f'Aritmetična sredina: {st_vzorcev_neodvisnih_avtorjev.mean():.2f}')
    print(f'Mediana: {st_vzorcev_neodvisnih_avtorjev.median()}')
