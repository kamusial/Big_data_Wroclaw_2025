with open ("C:\\Users\\vdi-student\\Desktop\\Big_data_Wroclaw_2025\\Zjazd2_10_05_25\\rozliczenie.csv", "r") as file1:
    content = file1.readlines()
print(content)

for i in range(len(content)):
    print('przed splitem')
    print(content[i])
    content[i] = content[i].split(';')
    print('Po splicie')
    print(content[i])

print('\n\n\nPo wszystkim')
print(content)
print(content[4][1][2])

average = 0
total = 0
#2. Obliczenie sredniej wyplaty
for i in range(1, len(content)):
    print(content[i][1])
    total += int(content[i][1])
average = total / (len(content)-1)
print(round(average,2))

# 3. Liczba kobiet na macierzynskim

