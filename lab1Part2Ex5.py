"""5. Дана непустая последовательность ненулевых целых чисел, за которой следует 0. Определить, сколько раз в этой последовательности меняется знак."""
from random import sample

n = int(input('введите размер списка (максимум 50): \n'))
list = sample(range(-25, 25), n)

print("Список", list)

i = 0
counter = 0
for i in range(1,len(list)):
        if list[i]*list[i-1] < 0:
            counter += 1
        elif list[i]*list[i-1] == 0:
            break

print("количество изменений знака", counter)