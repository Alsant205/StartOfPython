"""
Реализовать класс Stationery (канцелярская принадлежность).
● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
● в каждом классе реализовать переопределение метода draw. Для каждого класса
метод должен выводить уникальное сообщение;
● создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
"""


class Stationery:

    def __init__(self, title):
        self.title = title
        self.draw(title)

    def draw(self, title):
        print(f'Запуск отрисовки')


class Pen(Stationery):

    def draw(self, title):
        print(f'Пишем {self.title}')


class Pencil(Stationery):

    def draw(self, title):
        print(f'Рисуем {self.title}')


class Handle(Stationery):

    def draw(self, title):
        print(f'Выделяем {self.title}')


print('\nСообщение для метода pen.draw()')
pen = Pen('Ручкой')

print('\nСообщение для метода pencil.draw()')
pencil = Pencil('Карандашом')

print('\nСообщение для метода handle.draw()')
handle = Handle('Маркером')
