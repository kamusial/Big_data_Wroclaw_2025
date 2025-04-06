def stan_zdrowia(waga, wzrost: int, wiek, liczba_godzin_przed_pc, plec):
    if waga < 30 or wzrost < 80 or wiek < 16:
        return 0
    zdrowie = 100
    BMI = waga/(wzrost*wzrost)
    if BMI > 30:
        zdrowie -= 10
#        zdrowie = zdrowie - 10
    if wiek > 50:
        zdrowie -= (wiek - 50)
    if liczba_godzin_przed_pc > 4:
        zdrowie -= 2 * (liczba_godzin_przed_pc - 4)
    if plec == 'kobieta':
        zdrowie *= 1.1
    return zdrowie

print(f'Stan zdrowia: {stan_zdrowia(112, 70, 80, 16, "man")}')

