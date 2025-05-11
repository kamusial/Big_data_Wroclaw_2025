try:
    experience = int(input('Ile lat pracujesz tutaj?   '))
    points = int(input('Ile masz punktow?   '))
    level = points / experience
except ValueError:
    print('Wpisano zle wartosci')
    experience = 1
    points = 0
    level = points / experience
except ZeroDivisionError:
    level = 0

print(f'Twoj poziom to: {level}')