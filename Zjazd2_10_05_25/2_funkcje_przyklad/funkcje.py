users = {
    'Kamil': '1234',
    'GosiaXD': 'Wiosna',
    'max': 'max' }

def user_exists(user):
    if user in users.keys():
        return True
    return False

def correct_passwd(user, passwd):
    if users[user] == passwd:
        return True
    return False

def registration(user, password):
    users[user] = password
    print(f'Rejestracja {user} z haslem {password}')

def password_complexity_check(passwd):
    conditions = 0
    if not len(passwd) >= 6:
        print('Haslo za krotkie')
        conditions += 1
    if not '.' in passwd:
        print('Brak kropki w hasle')
        conditions += 1
    if passwd == passwd.lower():
        print('brak duzej litery')
        conditions += 1
    if passwd == passwd.upper():
        print('brak malej litery')
        conditions += 1
    print(f'Liczba problemow {conditions}')
    if conditions == 0:
        return True
    return False

