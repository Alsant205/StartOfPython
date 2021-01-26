"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных. """


class Date(object):

    def __init__(self, date_string: str):
        self.date_string = date_string

    def __str__(self):
        return f'{self.date_string}'

    # извлекает число, месяц, год, преобразовывает их тип к типу «Число» и возвращает в виде списка
    @classmethod
    def get_integer_from_str(cls, date_string):
        # преобразовывает в список с известными позициями элементов
        return cls.date_validator(list(map(int, date_string.split('-'))))

    # проводит валидацию числа, месяца и года (например, месяц — от 1 до 12)
    @staticmethod  # вызывается Класс.метод(значение для обработки в методе)
    def date_validator(date_elements_list):
        if 1 < int(date_elements_list[0]) > 31:
            return 'Day is not valid'
        if 1 < int(date_elements_list[1]) > 12:
            return 'Month is not valid'
        if 1900 < int(date_elements_list[2]) > 2100:
            return 'Year is not valid'
        else:
            return 'Date is valid'


# сздаем экземпляр и сразу обращаемся к методу класса для извлечения отдельных значений из строки даты
date_1 = Date.get_integer_from_str('2-2-4912')
print(date_1)
