# przyjmie nazwe pliku (bez rozszerzenia)
# przyjmie rozszerzenie
# powie, czy rozszerzenie dozwolone - jeśli nie, to podaj inne
# program napisze ładnie nazwe z rozszerzeniem
# program wykona to dla X plików danych razem

def extention_correct(ext):
    if ext in extentions:
        return True
    return False

counter_attempt = 0
extentions = ['txt', 'csv', 'jpg', 'mp3']
filename = input('Podaj nazwe pliku:  ')

while True:
    extname = input('Podaj rozszerzenie:  ')
    if extention_correct(extname):
        print('Rozszerzenie obslugiwane')
        break
    else:
        counter_attempt += 1
        if counter_attempt > 3:
            print('Zle rozszerzenie 4 razy - przyjmuje txt')
            extname = 'txt'
            break
        print(f'Zle rozszerzenie po raz {counter_attempt}, jeszcze raz')


print(f'Plik: {filename}.{extname}')

