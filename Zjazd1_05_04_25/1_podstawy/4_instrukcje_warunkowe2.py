# Tutaj pisz swój kod, młody padawanie ;-)
print('Pierwszy program')

imie = input('Jak masz na imie?   ')
wiek = int(input('Ile masz lat?   '))
counter = 5  # dodatkowa zmienna, któa nic nie znaczy
# print('Siema',imie,'. Witamy na pokladzie')
# print('Siema {imie}, witamy na pokladzie')

if wiek > 18 and counter == 5:
    print('jesteś dorosly, witamy na pokladzie')
elif wiek == 18 or counter < 0:
    print('Mlody dorosly')
elif wiek >= 0:
    print(f'Siema {imie}, masz {wiek} lat, witamy na pokladzie')
    print(f'Bedziesz dorosly za {18 - wiek} lat')
else:
    print('Za mlody - blad')

print('koniec programu')
