"""15. Определить есть ли среди заданных целых чисел A, B, C, D хотя бы одно чётное."""
a = int(input('введите первое число: \n'))
b = int(input('введите второе число: \n'))
c = int(input('введите третье число: \n'))
d = int(input('введите четвертое число: \n'))
if (a % 2 == 0) or (b % 2 == 0) or (c % 2 == 0) or (d % 2 == 0):
    print("Да есть четное число")
else:
   print("Нет четных чисел")