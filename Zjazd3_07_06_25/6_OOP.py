# system do zarządzania wynikami  uczniów

# klasa uczen
# klasa test
# klasa system testowy – zarządza uczniami i wynikami, umożliwia zapis i odczyt plików.

class Uczen:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'


class Test:
    def __init__(self, uczen, przedmiot, wynik):
        self.uczen = uczen
        self.przedmiot = przedmiot
        self.wynik = wynik


    def __str__(self):
        return f'{self.uczen} | {self.przedmiot}: {self.wynik}%'


# Klasa zarządzająca testami i obsługą plików
class SystemTestowy:
    def __init__(self):
        self.lista_testow = []

    def dodaj_test(self, test):
        self.lista_testow.append(test)

    def zapisz_do_pliku(self, nazwa_pliku):
        with open(nazwa_pliku, 'w', encoding='utf-8') as f:
            for test in self.lista_testow:
                f.write(f"{test.uczen.imie};{test.uczen.nazwisko};{test.przedmiot};{test.wynik}\n")

# def wczytaj_z_pliku

    def wypisz_testy(self):
        for test in self.lista_testow:
            print(test)


system = SystemTestowy()

uczen1 = Uczen('Anna', 'Nowak')
test11 = Test(uczen1, 'Matematyka', 89)
test12 = Test(uczen1, 'Fizyka', 69)

uczen2 = Uczen('Tomasz', 'Lis')
test21 = Test(uczen2, 'Fizyka', 76.6)

system.dodaj_test(test11)
system.dodaj_test(test12)
system.dodaj_test(test21)

system.wypisz_testy()

system.zapisz_do_pliku('testy_uczniow.txt')

