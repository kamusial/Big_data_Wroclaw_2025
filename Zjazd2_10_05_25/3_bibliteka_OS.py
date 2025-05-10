import os
import time

print(os.getcwd())
os.chdir('C:\\Users\\vdi-student\\Desktop')
print(os.getcwd())
time.sleep(1)
os.mkdir('new folder')
time.sleep(1)
os.rename('new folder','Kamil')
time.sleep(1)
os.rmdir('Kamil')

os.system('cmd /c "cd C:\\Users\\vdi-student\\Desktop && dir /s new.txt >> result.txt"')