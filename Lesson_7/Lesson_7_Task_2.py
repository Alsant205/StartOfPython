from abc import ABC, abstractmethod
# from re import findall
import re

"""2) Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и
костюм. У этих типов одежды существуют параметры: размер (для пальто)и рост (для костюма). Это могут быть обычные
числа: V и H,соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (
V/6.5 + 0.5),для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий подсчет
расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных
классов проекта, проверить на практике работу декоратора @property. """


class Dress(ABC):
    @property
    @abstractmethod
    def dress(self):
        return 'its consumption calculator in Dress'

    def __init__(self, atr: int):
        self.atr = atr  # размер или рост

    def __add__(self, other):
        s = '.'.join(re.findall(r'\d+', str(self)))
        f = '.'.join(re.findall(r'\d+', str(other)))
        total = f'Общий расход ткани составит: {float(s) + float(f):.2f}'
        return total

    def __str__(self):
        return f'Расход ткани составит: {self.atr / getattr(self, "formula_1") + getattr(self, "formula_2"):.2f}'


# V/6.5 + 0.5 - формула для определения расхода ткани по размеру V для пальто
class Coat(Dress):
    formula_1 = 6.5
    formula_2 = 0.5

    @property
    def dress(self):
        return super().dress

    def consumption(self):
        return f'Расход ткани на пальто размера {self.atr} составит: {self.atr / 6.5 + 0.5:.2f}'


# 2*H + 0.3 - формула для определения расхода ткани по росту H для костюма
class Suit(Dress):
    formula_1 = 2
    formula_2 = 0.3

    @property
    def dress(self):
        return super().dress

    def consumption(self):
        return f'Расход ткани на костюм для роста {self.atr} составит: {self.atr * 2 + 0.3:.2f}'


coat_1 = Coat(1)
suit_1 = Suit(1)

print(coat_1)
print(suit_1)
print(coat_1 + suit_1)
