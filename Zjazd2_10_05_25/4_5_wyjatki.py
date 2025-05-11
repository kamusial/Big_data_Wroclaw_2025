data = input('Wpisz dane:  ')
try:
    data = int(data)
    print('Wpisana dana jest typu int')
except ValueError:
    try:
        data = float(data)
        print('Wpisana dana jest typu float')
    except:
        print('Zostaje string')