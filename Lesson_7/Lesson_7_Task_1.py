"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д. """


class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __add__(self, other):
        print('Результат сложения матриц через print(matrix_1 + matrix_2 +...)')

        # считает размерность исходной матрицы по столбцам для новой матрицы
        matrix_size = len(self.matrix_list[0])

        # создает новую матрицу для заполнения
        result_matrix = [[0] * matrix_size for _ in range(len(self.matrix_list))]
        stroka = -1  # счетчик строк в новой матрице для дальнейшего построчного запонления

        # распаковка исходных матриц построчно
        for left_arg_string, right_arg_string in zip(self.matrix_list, other.matrix_list):
            el_position = 0  # установливет указатель номера очередной позиции в новой матрице для заполнения
            # далее заполнение новой матрицы
            stroka += 1  # следующая строка для заполнения
            # распаковка исходных строк
            for elem_left_arg_string, elem_right_arg_string in zip(left_arg_string, right_arg_string):
                result_matrix[stroka][el_position] = elem_left_arg_string + elem_right_arg_string
                el_position += 1  # следующая позиция в строке для заполнения

        return Matrix(result_matrix)

    def __str__(self):
        return '\n'.join([f'{str(row[0])}    {str(row[1])}' for row in self.matrix_list])


matrix_1 = Matrix([
    [1, 2],
    [3, 4],
    [5, 1]
])

matrix_2 = Matrix([
    [7, 8],
    [9, 10],
    [11, 12]
])

# при выводе матрицы на экран она должна выглядеть как:
# 1  2
# 3  4
# 5  6

print(matrix_1)
print(matrix_1 + matrix_2)
