class Zwierze:
    def __init__(self, imie):
        self.imie = imie

    def przedstaw_sie(self):
        print(f"Cześć! Jestem zwierzęciem. Nazywam się {self.imie}.")

class Pies(Zwierze):
    def szczekaj(self):
        print(f"{self.imie} mówi: Hau hau!")

class Kot(Zwierze):
    def miaucz(self):
        print(f"{self.imie} mówi: Miau!")

pies = Pies('Reksio')
kot = Kot('Mruczek')

pies.przedstaw_sie()
pies.szczekaj()

kot.przedstaw_sie()
kot.miaucz()