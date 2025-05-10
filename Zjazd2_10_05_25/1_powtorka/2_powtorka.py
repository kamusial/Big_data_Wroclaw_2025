number_of_grades = int(input('Podaj liczbę ocen: '))
grades = []

for i in range(number_of_grades):
    grade = float(input(f'Podaj ocenę {i + 1}'))
    grades.append(grade)  #dodanie na koniec listy

avg = sum(grades) / number_of_grades
max_grade = max(grades)
min_grade = min(grades)

print(f"Średnia ocen: {avg}")
print(f"Maksymalna ocena: {max_grade}")
print(f"Minimalna ocena: {min_grade}")

