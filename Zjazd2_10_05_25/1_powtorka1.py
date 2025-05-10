# program pyta o liczbe ocen i liczy srednia
# wypisuje max i minimalna ocene
from numpy.ma.extras import average

number_of_grades = int(input('Ile jest ocen?  '))

sum = 0
for _ in range(number_of_grades):
    grade = int(input('prowadz ocene: '))
#    sum = sum + grade
    sum += grade

average_grade = sum / number_of_grades
print(f'Średnia ocena: {average_grade}')



