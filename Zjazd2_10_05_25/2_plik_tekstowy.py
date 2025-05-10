# liczba slow
# liczba unikalnych slow
# liczba zdan
# liczba pustych linii
# ile razy powtarza się slowo X

chars_to_remove = ['.', ',','(']
chars_to_remove2 = set('.,()/\\')


with open ("C:\\Users\\vdi-student\\Desktop\\Big_data_Wroclaw_2025\\Zjazd2_10_05_25\\text.txt", "r", encoding='utf-8') as file1:
    content = file1.read()
no_of_docs = content.count('.')
print(f'Liczba zdan: {no_of_docs}')

content = content.replace('(','').replace('.','')
content = content.lower()
content = content.split()
print(content)

print(f'Liczba slow: {len(content)}')
print(f'Liczba unikalnych slow: {len(set(content))}')

words = {}
for word in content:
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
print(f'Liczba roznych slow: {len(words)}')
print(f'Slowo peppers powtarza sie {words["peppers"]} razy')