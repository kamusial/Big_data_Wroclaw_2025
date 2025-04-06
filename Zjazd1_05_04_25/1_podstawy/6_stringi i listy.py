napis = 'Witamy w sobote'
print(napis)
print(napis[4])  # 5ta litera
print(napis[-1])   # ostatnia litera
print(napis[-2])   # przedostatnia litera

print(napis[ 3  : 8 ])   # od, do

plik = input('Podaj nazwe pliku z rozszerzeniem:    ')
nowa_nazwa = plik[ : -4] + '_01' + plik[-4 : ]
print(f'Nowa nazwa to: {nowa_nazwa}')

