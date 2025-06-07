import pandas as pd

class DanePlikowe:
    def __init__(self, sciezka):
        self.sciezka = sciezka
        self.dane = None

    def pokaz_podsumowanie(self):
        if self.dane is not None:
            print(self.dane.head())
        else:
            print('Brak danych')

class DanePracownicyCSV(DanePlikowe):
    def wczytaj(self):
        try:
            self.dane = pd.read_csv(self.sciezka, sep=';')
            print('Dane CSV zaladowane.')
        except Exception as e:
            print(f'Blad przy wczytywany CSV: {e}')

    def filtruj_pensje(self, prog):
        return self.dane[self.dane['wyplata'] >= prog]

class DanePracownicyTXT(DanePlikowe):
    def wczytaj(self):
        try:
            self.dane = pd.read_csv(self.sciezka, sep='\t')
            print('Dane TXT wzcytane')
        except Exception as e:
            print(f'Blad przy wczytywany TXT: {e}')

    def zapisz_do_csv(self, nowy_plik):
        if self.dane is not None:
            self.dane.to_csv(nowy_plik, index=False)
            print(f'Dane zapisane do {nowy_plik}')

csv_dane = DanePracownicyCSV('dane10OOP.csv')
csv_dane.wczytaj()
csv_dane.pokaz_podsumowanie()
print('Filtruje, powyzej 4k')
przefiltrowani = csv_dane.filtruj_pensje(4000)
print(przefiltrowani)

txt_dane = DanePracownicyTXT('dane10OOP.txt')
txt_dane.wczytaj()
txt_dane.pokaz_podsumowanie()

txt_dane.zapisz_do_csv('csv_z_txt.csv')