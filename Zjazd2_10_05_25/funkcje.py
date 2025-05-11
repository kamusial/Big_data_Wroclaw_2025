def can_be_int(x):
    try:
        int_x = int(x)
        return True
    except ValueError:
        return False


def can_be_float(x):
    try:
        float_x = float(x)
        return True
    except ValueError:
        return False

# funkcja analizująca tekst
# funkcja sprawdzająca liczbe słów w tekście