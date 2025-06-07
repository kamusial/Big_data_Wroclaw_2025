class Platnosc:
    def __init__(self, kwota):
        self.kwota = kwota
        self.id = 0

    def wykonaj(self):
        print(f"Przetwarzanie płatności na kwotę {self.kwota} zł...")

    def cofnij(self):
        pass

    def pokaz_status(self):
        pass

class PlatnoscKarta(Platnosc):
    def __init__(self, kwota, numer_karty):
        super().__init__(kwota)
        self.numer_karty = numer_karty

    def wykonaj(self):
        print(f'Autoryzajca karty {self.numer_karty[-4:]}...')
        super().wykonaj()
        print(f'Platnosc zakonczona.')

class PlatnoscBlik(Platnosc):
    def __init__(self, kwota, kod_blik):
        super().__init__(kwota)
        self.kod_blik = kod_blik

    def wykonaj(self):
        print(f'Weryfikacja kodu BLIK {self.kod_blik}...')
        super().wykonaj()
        print(f'Platnosc blik zakonczona.')

p1 = PlatnoscKarta(120.50, '1234-1234-1234-1234')
p2 = PlatnoscBlik(80.00, '989898')

p1.wykonaj()
print()
p2.wykonaj()
