"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
завершиться с ошибкой. """


class DivisionByZero(Exception):
    """"Обработчик исключения деления на ноль"""
    def __init__(self):
        pass

    def __str__(self):
        self.txt = 'Ошибка! Деление на ноль.'
        return self.txt


try:
    c = int(input('Делим единицу. Введите число делитель:\n'))
except ValueError as v_err:
    print('Требуется число.', v_err)
else:
    try:
        if c == 0:
            raise DivisionByZero()
        a = 1 / c
    except DivisionByZero as my_err:
        print(my_err)
    except ValueError as v_err:
        print(v_err)
    else:
        print(f'Число делитель: {c}\n1 / {c} = {a:.4f}')
