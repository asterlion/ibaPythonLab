a = int(input('введите первую сторону прямоугольника в см: \n'))
b = int(input('введите вторую сторону прямоугольника в см: \n'))
n = 0


def Squares(a, b, n):
    if (a == b):
        print("Этот прямоугольник - квадрат со сторонами:", a, "и", b)
        print("Количество нарезанных фигур:", n + 1)
        return n + 1
    elif (a < b):
        print("Следующий прямоугольник:", n + 1,"й")
        print("Стороны прямоугольника:", a, "и", b, "\n")
        return Squares(a, b - a, n + 1), n
    else:
        print("Следующий прямоугольник:", n + 1,"й")
        print("Стороны прямоугольника:", a, "и", b, "\n")
        return Squares(a - b, b, n + 1), n


Squares(a, b, n)
