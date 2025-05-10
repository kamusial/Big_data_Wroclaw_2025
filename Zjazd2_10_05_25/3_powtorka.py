grades = []

while True:
    decission = input('Czy chcesz wprowadzic ocene?   T/N   ')
    if decission.lower() == 't':
        grade = float(input('Dodaj ocene:  '))
        grades.append(grade)
    elif decission.lower() == 'n':
        print('Wychodze')
        break
    else:
        print('Nie rozpoznano wyboru')

print('koniec programu')