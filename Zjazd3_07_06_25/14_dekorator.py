import time

def mierz_czas(funkcja):
    def wrapper(*args, **kwargs):
        start = time.time()
        wynik = funkcja(*args, **kwargs)
        stop = time.time()
        print(f"Czas wykonania funkcji {funkcja.__name__}: {stop - start:.4f} sekund")
        return wynik
    return wrapper

@mierz_czas
def przykladowa_funkcja(n):
    iloczyn = 1
    for i in range(1, n+1):
        iloczyn *= i
        iloczyn /= i
    print(f'Wynik mnozenia: {iloczyn}')
    return iloczyn

przykladowa_funkcja(100000)