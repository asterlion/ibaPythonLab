"""3. Удалить элементы, индексы которых кратны 7."""
import random
from random import sample

n = int(input('введите размер списка: \n'))
list = sample(range(0, 99), n)

print("Список", list)

b = []
i = 6
j = 0
while i < (len(list) + j):
    b.append(list[i-j])
    list.pop(i-j)
    i = i + 7
    j = j + 1
    print(i)

print("A =", list)
print("B =", b)
