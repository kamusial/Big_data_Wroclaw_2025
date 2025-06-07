print('SiemaMerito')

komunikat = 'Zostales zalogowany i juz'
print(komunikat)
print(komunikat[4])   # litera 'a'
print(komunikat[9:19])   # slowo 'zalogowany'

nowy_komunikat = 'siema ' + komunikat[9:19]
print(nowy_komunikat)   # 'siema zalogowany

for i in range(len(nowy_komunikat)):
    print(f'Powtorzenie {i+1}: litera o indeksie {i}, to {nowy_komunikat[i]}')

if nowy_komunikat[-1] != 'a':
    print('Witam Pana')
else:
    print('Witam Panią')


data = input('Wprowadz nazwy, rozdzielone spacją:  ').split()
print(data)
filename = input('Wprowadz nazwe pliku:  ').split('.')
print(filename)
