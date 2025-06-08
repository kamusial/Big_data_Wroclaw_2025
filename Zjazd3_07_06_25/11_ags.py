def licz_BMI(waga, wzrost=170):
    return wzrost / waga / waga

def suma(*liczby):
    sum = 0
    for liczba in liczby:
        sum += liczba
    return sum

def suma2(liczby):
    sum = 0
    for liczba in liczby:
        sum += liczba
    return sum

print(suma(2, 3))
print(suma(2, 3, 7, 4, 2, 1))
print(suma2([2, 3, 7, 4, 2, 1]))
print('\nprzyklad2')

students = [1234, 4352, 6543, 1246, 5986]
absolwents = [4242, 4352, 6543,1256, 6666, 5555, 4321]
students_with_debt = [6543, 5986, 4321]

def student_info(index_number):
    if index_number in students:
        print(f'Osoba {index_number} studiuje')
    if index_number in absolwents:
        print(f'Osoba {index_number} ukonczyla studia')
    if (index_number in students) or (index_number in absolwents) and \
            (index_number in students_with_debt):
        print(f'Osoba {index_number} zalega z kasą')
    if (index_number not in students) or (index_number not in absolwents) and \
            (index_number in students_with_debt):
        print(f'Osoba {index_number} - błąd')

student_info(5986)