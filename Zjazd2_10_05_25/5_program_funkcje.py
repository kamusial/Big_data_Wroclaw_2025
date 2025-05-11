from funkcje import *
# import funkcje

points = input('Ile masz punktow?   ')
if can_be_int(points):
    print('Masz calkowita liczbe punktow')
elif can_be_float(points):
    print('Doprowadz do calkowitewj liczby punktow')
else:
    print('Zle podane punkty')
