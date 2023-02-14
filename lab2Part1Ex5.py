"""Лаб 2
Вариант 5
Найдите наименьший четный элемент списка. Если такого нет, то выведите первый элемент.
Преобразовать список так, чтобы сначала шли нулевые элементы, а затем все остальные.
"""
from random import sample

n = int(input('введите размер списка (максимум 20): \n'))
list1 = sample(range(-10, 10), n)
list2 = sample(range(-10, 10), n)
list3 = sample(range(-10, 10), n)
list = list1 + list2 + list3

print("Список", list)

i = 0
min = list[0]
for i in range(0, len(list)):
    if list[i] % 2 == 0 and list[i] <= min:
        min = list[i]

print("минимальный четный элемент", min)
i = 0
j = 0
listNew = []

while i < len(list):
    if list[i] == 0:
        listNew.append(j)
        del list[i]
        i += 1
    else:
        i += 1
list = listNew + list
print("Список", list)
