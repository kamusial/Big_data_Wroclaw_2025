# przyjmie nazwe pliku (bez rozszerzenia)
# przyjmie rozszerzenie
# powie, czy rozszerzenie dozwolone - jeśli nie, to podaj inne
# program napisze ładnie nazwe z rozszerzeniem
# program wykona to dla X plików danych razem

extentions = ['txt', 'csv', 'jpg', 'mp3']

filename = input('Podaj nazwe pliku:  ')

while True:
    extname = input('Podaj rozszerzenie:  ')
    if extname in extentions:
        print('Rozszerzenie obslugiwane')
        break
    else:
        print('Zle rozszerzenie, jeszcze raz')

print('Dalsza czesc programu')

