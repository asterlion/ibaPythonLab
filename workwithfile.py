# Скопировать в файл F2 только четные строки из F1. Подсчитать размер файлов F1 и F2 (в байтах).
import os

f1 = open('d:\Таня\IT\IBA\Python\F1.txt')
list = f1.readlines()
print("список", list)
f2 = open('d:\Таня\IT\IBA\Python\F2.txt', 'w')
f2.close()
i = 1
while i <= (len(list)-1):
    f2 = open('d:\Таня\IT\IBA\Python\F2.txt', 'a')
    f2.write(list[i])
    i = i + 1
f1.close()
f2.close()
