"""11. Удалить пять первых нечетных по значению элементов списка."""
import random

a = []
n = int(input('введите размер массива: \n'))
for i in range(n):
    n = round(random.random() * 100)
    a.append(n)
print("A =", a)

b = []
i = 0
j = 0
while i < len(a) and j < 6:
    if a[i] % 2 != 0:
        b.append(a[i])
        del a[i]
        j += 1
    else:
        i += 1

print("A =", a)
print("B =", b)
