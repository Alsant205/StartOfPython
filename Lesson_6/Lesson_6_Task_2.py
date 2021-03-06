"""2.
Реализовать класс Road (дорога).
● определить атрибуты: length (длина), width (ширина);
● значения атрибутов должны передаваться при создании экземпляра класса;
● атрибуты сделать защищёнными;
● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
дороги асфальтом, толщиной в 1 см*число см толщины полотна;
● проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""


class Road:

    def __init__(self, a, b):
        self._length = a
        self._width = b
        self.asf_weight()

    def asf_weight(self):
        layer = int(input('Какова толщина асфальта в сантиметрах? \n'))
        weight = self._length * self._width * 25 * layer
        print(f'Масса асфальта для покрытия дороги толщиной {layer} см составляет {int(weight / 1000)} тонн.')


new_road = Road(5000, 20)  # при толщине 5 см масса асфальта должна составить 12500 тонн
