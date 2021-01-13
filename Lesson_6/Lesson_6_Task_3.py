"""
Реализовать базовый класс Worker (работник).
● определить атрибуты: name,surname, position (должность), income (доход);
● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
● создать класс Position (должность) на базе класса Worker;
● в классе Position реализовать методы получения полного имени сотрудника
(get_full_name)и дохода с учётом премии (get_total_income);
● проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""


class Worker:

    def __init__(self, name, surname, wage, bonus):
        self.name = name
        self.surname = surname
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        print(self.name + ' ' + self.surname)

    def get_total_income(self):
        print(f'Доход составляет {self._income.get("wage") + self._income.get("bonus")} руб.')


new_pos = Position('Сидор', 'Петров', 1000, 10)
print(f'Экземпляр new_pos класса Position:\n{new_pos}')

print(f'\nВызов метода get_full_name экземпляра new_pos')
new_pos.get_full_name()

print('\nВызов метода get_total_income экземпляра new_pos')
new_pos.get_total_income()

print(f'\nПроверка значения атрибута new_pos.name\n{new_pos.name}')

print(f'\nПроверка значения атрибута new_pos.surname\n{new_pos.surname}')

print(f'\nПроверка значения атрибута new_pos._income\n{new_pos._income}')
