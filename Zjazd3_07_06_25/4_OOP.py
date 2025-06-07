class Auto:

    def __init__(self, kolor, wiek):
        self.kolor = kolor
        self.ilosc_paliwa = 10
        self.tryb_ekonomiczny = False
        self.spalanie_na_100 = 14
        self.rocznik = 2025 - wiek
        self.mandaty = []
        self.komentarze = []

    def zasieg(self):
        zasieg = self.ilosc_paliwa / self.spalanie_na_100 * 100 * 0.9
        return round(zasieg)

    def ustaw_tryb(self, tryb):
        if tryb == 'eco':
            self.tryb_ekonomiczny = True
            self.spalanie_na_100 = 10
            print('Ustawiono eco')


bmw1 = Auto('blue', 12)
print(bmw1.kolor)
bmw1.kolor = 'red'
print(f'nowy kolor {bmw1.kolor}')
print(f'Auto spala {bmw1.spalanie_na_100} i  tryb eco jest {bmw1.tryb_ekonomiczny}')

audi45 = Auto('black', 8)
print(f'Auto ma {audi45.ilosc_paliwa} paliwa')
print(f'Zasieg audi: {audi45.zasieg()}')

#     def sdfsdfsdfsd