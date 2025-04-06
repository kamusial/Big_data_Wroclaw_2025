new_users = {
    'Zofia': 'Zosia01',
    'Adrian': 'xxx',
    'Maciej': '1234',
    'Kinga': 'KKK'
}

# program do logowania i dodawania nowych uzytkownikow
while True:
    username = input('podaj nazwe uzytkownika:   ')
    if username in new_users.key():
        passwd = input('Podaj haslo:   ')
        if passwd == new_users[username]:
            break
    else:
        decission = input('Czy chcesz dodać uzytkownika? y/n ')
        if decission == 'y':
            new_users[username] = '12345'
            print(f'dodano uzytkownika {username} z haslem {new_users[username]}')


