"""11. Даны три числа a, b, c. Значение наибольшего из них присвоить переменной d."""
a = int(input('введите первое число: \n'))
b = int(input('введите второе число: \n'))
c = int(input('введите третье число: \n'))
if abs(a) >= abs(c) and abs(a) >= abs(b):
    d = a
    print(d)
elif abs(b) >= abs(c) and abs(b) >= abs(a):
    d = b
    print(d)
else:
    d = c
    print(d)
