lista_imion = ['Kamil', 'Darek', 'Zofia', 'Kasia', 'Kinga']
# program informuje, ile jest Pań na liście

licznik_panie = 0
for i in range(len(lista_imion)):
    if lista_imion[i][-1] == 'a':
        print(f'Pani {lista_imion[i]}')
        licznik_panie = licznik_panie + 1
    else:
        print(f'Pan {lista_imion[i]}')
print(f'Liczba Pań na liscie: {licznik_panie}')

icznik_panie = 0
for imie in lista_imion:
    if imie[-1] == 'a':
        print(f'Pani {imie}')
        licznik_panie = licznik_panie + 1
    else:
        print(f'Pan {imie}')
print(f'Liczba Pań na liscie: {licznik_panie}')





