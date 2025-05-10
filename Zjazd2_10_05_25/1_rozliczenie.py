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
