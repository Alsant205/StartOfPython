"""7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса (
комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного
результата. """


# ------------------------------------------ вариант 1 ------------------------------------------
class ComplexNumbers1:
    def __init__(self, r):
        self.r = r

    def __str__(self):
        return f'{self.r}'

    def __add__(self, other):
        return self.r + other.r

    def __mul__(self, other):
        return self.r * other.r


com_digit_1 = ComplexNumbers1(complex(1, 2))
com_digit_2 = ComplexNumbers1(complex(3, 4))

print('\nВариант 1')
print('Даны два комплексных числа: ', com_digit_1, com_digit_2)
print('сложение ', end='')
print(com_digit_1 + com_digit_2)
print('умножение ', end='')
print(com_digit_1 * com_digit_2)
print()


# ------------------------------------------ вариант 2 ------------------------------------------
class ComplexNumbers2:
    def __init__(self, x, y):  # принимает два аргумента
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self}'

    def __add__(self, other):
        a = self.x + other.x  # по формуле (x1+x2)+(y1+y2)i
        b = self.y + other.y
        return complex(a, b)

    def __mul__(self, other):  # по формуле (x1⋅x2−y1⋅y2)+(x1⋅y2+x2⋅y1)i
        a = self.x * other.x - self.y * other.y
        b = self.y * other.x + self.x * other.y
        return complex(a, b)


com_digit_11 = ComplexNumbers2(1, 2)
com_digit_22 = ComplexNumbers2(3, 4)

print('Вариант 2')
print('Даны два объекта с атрибутами:', 'ComplexNumbers2(1, 2)', 'ComplexNumbers2(3, 4)')
print('сложение ', end='')
print(com_digit_11 + com_digit_22)
print('умножение ', end='')
print(com_digit_11 * com_digit_22)
