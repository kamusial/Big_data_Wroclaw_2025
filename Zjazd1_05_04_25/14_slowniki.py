usernames = ['Zofia', 'Adrian', 'Maciej', 'Kinga']
passwds = ['Zosia01', 'xxx', '1234', 'KKK']

users = [
    ['Zofia', 'Zosia01'],
    ['Adrian', 'xxx'],
    ['Maciej', '1234'],
    ['Kinga', 'KKK']
]
print(f' Uzytkownik {users[2][0]} ma haslo {users[2][1]}')

new_users = {
    'Zofia': 'Zosia01',
    'Adrian': 'xxx',
    'Maciej': '1234',
    'Kinga': 'KKK'
}

zakupy = {'marchew': 4, 'seler': 2, 'mleko': 12, 'serek': 4}

print(zakupy)
print(zakupy.items())
print(zakupy.keys())
print(zakupy.values())
print(zakupy['seler'])    # wartosc dla selera
zakupy['majonez'] = 1    # doda 1 majones do słownika
zakupy['seler'] = 5      # nadpisze seler
zakupy['majonez'] += 1   # dodaj jeszcze jedne majonez
print(zakupy)







