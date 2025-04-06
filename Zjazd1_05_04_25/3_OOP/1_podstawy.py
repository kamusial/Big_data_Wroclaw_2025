def przywitanie():
    print('Witamy na pokladzie')

def przygotowanie_srodowiska(imie, nazwisko, id):
    print(f'tworzenie maila {imie}.{nazwisko}@firma.com')
    print('format systemu')
    print('Przygotowanie maszyny wirtualnej')
    print(f'Tworzenie folderu na dysku sieciowym, folder: {imie}_{id}')


print('Nowy program')
przygotowanie_srodowiska('Kamil', 'Musial', 123)