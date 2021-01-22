"""3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо
только числами. Класс-исключение должен контролировать типы данных элементов списка."""
"""Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
скрипта, введя, например, команду «stop». При этом скрипт завершается, сформированный список с числами выводится на
экран."""
"""Подсказка: для этого задания примем, что пользователь может вводить только числа и строки. Во время ввода
пользователем очередного элемента необходимо реализовать проверку типа элемента. Вносить его в список, только если
введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее
сообщение. При этом работа скрипта не должна завершаться. """


class DigitOnly(Exception):
    def __init__(self):
        # self.n = n
        pass

    def __str__(self):
        self.n = 'Ошибка! Требуются только числа.\n'
        return self.n

    @staticmethod
    def checker(subj):
        try:
            if subj is int and abs(int(subj)) or float(subj):
                return subj
        except (TypeError, ValueError):
            raise DigitOnly
        else:
            return subj


numbers_collection = []
print('Для выхода введите "q"')
while True:
    # print(numbers_collection)
    get_num = input('Введите число\n')
    if get_num != 'q':
        # DigitOnly.checker(get_num)
        try:
            DigitOnly.checker(get_num)
            # numbers_collection.append(float(get_num)) if '.' in get_num else numbers_collection.append(int(get_num))
            if '.' in get_num:
                numbers_collection.append(float(get_num))
            else:
                numbers_collection.append(int(get_num))
        except DigitOnly as dig_on:
            print(dig_on)
    else:
        print('Сформирован список: ', numbers_collection)
        break
