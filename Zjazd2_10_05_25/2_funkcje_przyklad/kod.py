from funkcje import *



while True:
    user = input('Podaj uzytkownika: ')
    passwd = input('Podaj haslo: ')
    if user_exists(user):
        if correct_passwd(user, passwd):
            print('Poprawne dane')
            break
        else:
            print('bledne haslo')
    else:
        print('Uzytkownik nie istnieje')
        decission = input('Zarejestrowac? T/N')


print('Witamy w systemie')