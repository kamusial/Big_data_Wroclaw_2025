extentions = ['txt', 'csv', 'jpg', 'mp3']

def extention_correct(ext):
    if ext in extentions:
        return True
    return False

def add_extention(new_ext):
    # sprawdzic czy rozszerzneie poprawne, czy już na liście

    extentions.append(new_ext)

