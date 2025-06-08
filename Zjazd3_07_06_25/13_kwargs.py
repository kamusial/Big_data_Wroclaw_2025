import random

emp_ids = [1234, 1235, 1236]

def zarejestruj_pracownika(**dane_pracownika):
    mail = dane_pracownika['imie']+'.'+dane_pracownika['nazwisko']+'@firma.com'
    print(mail)
    emp_ids.append(emp_ids[-1]+1)
    print(emp_ids[-1])

zarejestruj_pracownika(imie='Kamil', nazwisko='Kowalski',wiek=32, zawod='syn')

students = {1234: [False, 4.32], 2345: [True, 2.65], 6543: [True, 2.2]}

def show_info(*dane, **parameters):

show_info(1234, 2345, dept=True, max_grades=2, failing='all')
