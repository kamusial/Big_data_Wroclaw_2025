while True:
    username = input('Wprowadz nazwe uzytkownika:  ')
    if username == 'Kamil1':
        print('Poprawny uzytkownik')
        passwd = input('Wprowadz haslo:  ')
        if passwd == '1234':
            break
    elif username == 'AdminAdmin':
        print('Wchodzisz jako administrator')
        break


print('Witamy w programie')

