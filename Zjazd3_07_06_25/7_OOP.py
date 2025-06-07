#  biblioteka

# książka, czytelnik, biblioteka

class Ksiazka:
    def __init__(self, tytul, autor):
        self.tytul = tytul
        self.autor = autor
        self.wypozyczona = False

    def __str__(self):
        status = 'Wypozyczona' if self.wypozyczona else 'Dostepna'
        return f'{self.tytul} - {self.autor} ({status})'


class Czytelnik:
    def __init__(self, imie):
        self.imie = imie
        self.wypozyczone = []

    def __str__(self):
        return f'{self.imie}, wypozyczone ksiazki: {len(self.wypozyczone)}'

class Bilbioteka:
    def __init__(self):
        self.ksiazki = []

    def dodaj_ksiazke(self, ksiazka):
        self.ksiazki.append(ksiazka)

    def wypozycz(self, tytul, czytelnik):
        for ksiazka in self.ksiazki:
            if ksiazka.tytul == tytul and not ksiazka.wypozyczona:
                ksiazka.wypozyczona = True
                czytelnik.wypozyczone.append(ksiazka)
                print(f'{czytelnik.imie} wypozyczyl {tytul}')
                return
        else:
            print(f"Książka '{tytul}' jest niedostępna.")

    def pokaz_zasoby(self):
        print('Ksiazki w bibliotece:')
        for k in self.ksiazki:
            print(f'- {k}')

biblioteka = Bilbioteka()

biblioteka.dodaj_ksiazke(Ksiazka("Pan Tadeusz", "Adam Mickiewicz"))
biblioteka.dodaj_ksiazke(Ksiazka("Lalka", "Bolesław Prus"))
biblioteka.dodaj_ksiazke(Ksiazka("Pan Wolodyjowski", "Adam Mickiewicz"))

czytelnik = Czytelnik("Janek")

biblioteka.wypozycz("Lalka", czytelnik)
biblioteka.wypozycz("Lalka", czytelnik)  # Próba drugi raz

biblioteka.pokaz_zasoby()