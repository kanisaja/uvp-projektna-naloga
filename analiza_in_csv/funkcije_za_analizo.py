import pandas as pd
import matplotlib.pyplot as plt

vzorci = pd.read_csv('vzorci.csv', sep=',')


def korelacija_manjkanja_in_nizje_priljubljenosti(vzorci):
    for stolpec in vzorci.columns:
        if stolpec != 'Priljubljenost' and vzorci[stolpec].count() != 3000:
            vzorci[f'{stolpec} manjka'] = vzorci[stolpec].isnull()

    korelacije = {}
    for stolpec in vzorci.columns:
        if 'manjka' in stolpec:

            korelacija = vzorci['Priljubljenost'].corr(vzorci[stolpec])
            korelacije[stolpec] = korelacija

    korelacije_serija = pd.Series(korelacije)

    korelacije_serija.plot(kind='barh', x='Korelacija')
    plt.title('Korelacija med manjkajočimi podatki in nižjo priljubljenostjo')
    plt.show()
    print('Korelacija z višjo priljubljenostjo:')
    for kljuc, vrednost in korelacije.items():
        print(f'\t- {kljuc}: {vrednost:.3f}')
