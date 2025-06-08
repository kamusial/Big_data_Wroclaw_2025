import math

def total_distance(wind_level, rain_level, *coordinates):
    if len(coordinates) % 2 != 0:
        print(f'Nieprawidlowe koordynaty. Podałeś {len(coordinates)} wspołżędnych')
        return False
    x0 = 0
    y0 = 0
    distance = 0
    for i in range(0, len(coordinates), 2):
        x = coordinates[i]
        y = coordinates[i+1]
        print(f'trasa z {x0, y0} do {x, y}')
        distance += math.sqrt( (x0-x)**2 + (y0-y)**2 )
        x0, y0 = x, y
    print(f'Długosc trasy: {distance}')
    return distance

# print(total_distance(3, 2, 3, 6, 7))

total_distance(5, 3, 1, 1, 2, 2, 3, 3 )