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
    