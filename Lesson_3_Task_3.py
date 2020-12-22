"""
Реализовать функцию my_func(),
которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов
"""


def my_func(num_1, num_2, num_3):
    """возвращает сумму наибольших двух аргументов"""

    args = (num_1, num_2, num_3)
    a = min(num_1, num_2, num_3)
    b = sum(args) - a
    return b


print('\nВведите числа A B и C:\n')
a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))
print(my_func(a, b, c))
