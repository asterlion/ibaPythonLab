"""Лаб 2
2.	Симметричная матрица.
Дана квадратная матрица. Проверить, является ли она симметричной относительно главной диагонали.
"""
import random

n = int(input('Введите кол-во строк и столбцов матрицы: \n'))
"""вводим флаг, маркер в задачу"""
h = ('true')
matrix = []
"""для ввода матрицы из консоли
4
0 1 2 5
1 0 2 5
2 2 0 4
5 5 4 0

4
2 6 3 8
5 9 8 7
6 3 8 4
0 0 0 0
"""
for i in range(0, n):
    matrix.append(list(map(int, input().split())))
"""matrix = [[random.randrange(10) for i in range(n)] for j in range(n)]""" """для ранндомного ввода матрицы"""
for elem in matrix:
    print(elem)
for k in range(0, n):
    for l in range(1, n):
        if (matrix[k][l] != matrix[l][k]) and h == ('true'):
            """смотрим какие элементы сравнила программа"""
            print(matrix[k][l], matrix[l][k])
            h = ('False')

if h != ('False'):
    print('Матрица симметрична')
else:
    print('Обычная матрица')
