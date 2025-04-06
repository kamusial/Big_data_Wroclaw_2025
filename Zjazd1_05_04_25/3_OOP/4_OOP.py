class Employee:
    def __init__(self, first_name, nazwisko, zawod):
        self.first_name = first_name
        self.surname = nazwisko
        self.mail = f'{first_name}.{nazwisko}@firma.com'
        self.emp_id = 1
        self.profession = zawod
        self.skill = 5
        self.days_free = 26
        self.history = []

    def use_free_days(self, days):
        if self.days_free >= days:
            self.days_free -= days
            print(f'Wykorzystano {days} dni, zostało {self.days_free} dni')
        else:
            print(f'Masz {self.days_free} dni. Nie możesz wykorzystac {days}')

    def add_free_days(self, days):
        emp_id = input('Podaj swoje ID:   ')
        passwd = input('Podaj haslo:  ')
        if passwd == 'abc':
            self.days_free += days
            print(f'uzytkonik {emp_id} dodal {days} dni do puli {self.first_name}')



emp1 = Employee('Kamil', 'Musial', 'eng')
emp2 = Employee('Maryla', 'Rodowicz', 'singer')

print(emp1.emp_id)
print(f'Pracownicy to: {emp1.first_name}, {emp2.first_name}')

emp1.emp_id = 1234
emp1.skill += 1
print(emp1.emp_id, emp1.skill)
emp1.use_free_days(3)

