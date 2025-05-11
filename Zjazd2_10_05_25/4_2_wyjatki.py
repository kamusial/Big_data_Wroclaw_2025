try:
    experience = int(input('Ile lat pracujesz tutaj?   '))
except:
    print('Nie da sie, zakladam doswiadczenie = 1')
    experience = 1

try:
    points = int(input('Ile masz punktow?   '))
except:
    print('Nie da sie, zakladam liczbe punktow = 0')
    points = 0

try:
    level = points / experience
except:
    print('cos poszlo nie tak')
    level = 0

print(f'Twoj poziom to: {level}')