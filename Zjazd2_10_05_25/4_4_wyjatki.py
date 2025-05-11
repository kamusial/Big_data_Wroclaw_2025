while True:
    try:
        number = int(input('Wpisz numer indeksu:  '))
        break
    except ValueError:
        print('Zla wartosc, jeszcze raz')

print(f'Twoj numer indeksu to {number}')