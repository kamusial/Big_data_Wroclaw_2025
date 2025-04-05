# program sprawdza, czy produkt do kupienia jest w domu
# program tworzy listę zakupow
# program pozwala wyjsc w dowolnym momencie

produkty_na_stanie = ['machew', 'woda', 'soda', 'dlugopis', 'miod']
produkty_do_kupienia = []

while True:
    decission = input('Czy chcesz dodac produkt?   y/n')
    if decission == 'y':
        produkt = input('Wprowadz produkt:   ')
        if (produkt not in produkty_na_stanie) and (produkt not in produkty_do_kupienia):
            produkty_do_kupienia.append(produkt)
        else:
            print('Masz to w domu')
    else:
        break
print(f'Produkty do kupienia {produkty_do_kupienia}')
