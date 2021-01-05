from random import randint

"""4
Реализуйте базовый класс Car.
● у класса должны быть следующие атрибуты: speed,color,name,is_police (булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar,WorkCar,PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed.При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат. """


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print(f'{self.color} {self.name} is moving')

    def stop(self):
        print(f'{self.color} {self.name} is stops')

    def turn(self):  # случайным порядком определяем направление поворота
        n = randint(0, 1)
        print(f'{self.color} {self.name} turns to the left') if n == 0 else print(f'{self.color} {self.name} turns to '
                                                                                  f'the right')

    def show_speed(self):
        print(f'{self.name} current speed = {self.speed}')

    def movement(self):  # случайным порядком определяем действие экземпляра
        if self.is_police:
            print('Police ', end='')
        n = randint(0, 2)  # генерирует значения: 0 - стоп; 1 - вперед; 2 - поворот
        if n == 0:
            self.stop()
            print(f'{self.name} current speed = 0')
        elif n == 1:
            self.go()
            self.show_speed()
        else:
            self.turn()
            self.show_speed()


class TownCar(Car):
    speed_limit = 60
    is_police = False

    def show_speed(self):  # переопределяем метод для вывода предупреждения о превышении скорости
        if self.speed > self.speed_limit:
            print(f'Внимание! Превышение скорости на {self.speed - self.speed_limit} ки/ч.')
        else:
            print(f'{self.name} current speed = {self.speed}')


class SportCar(Car):
    speed_limit = None
    is_police = False


class WorkCar(Car):
    speed_limit = 40
    is_police = False

    def show_speed(self):  # переопределяем метод для вывода предупреждения о превышении скорости
        if self.speed > self.speed_limit:
            print(f'Внимание! Превышение скорости на {self.speed - self.speed_limit} ки/ч.')
        else:
            print(f'{self.name} current speed = {self.speed}')


class PoliceCar(Car):
    speed_limit = None
    is_police = True


car_1 = PoliceCar(20, 'black', 'Dodge', True)
PoliceCar.movement(car_1)
print()
car_2 = TownCar(30, 'white', 'Nissan', False)
TownCar.movement(car_2)
print()
car_3 = SportCar(30, 'red', 'Ferrari', False)
SportCar.movement(car_3)
print()
car_4 = WorkCar(50, 'grey', 'Ford', False)
WorkCar.movement(car_4)
