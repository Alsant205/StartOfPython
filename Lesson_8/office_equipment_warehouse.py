"""4. Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите параметры,
общие для приведённых типов. В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники. """
"""5. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение
компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру (например, словарь). """
"""6. Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества принтеров, 
отправленных на склад, нельзя использовать строковый тип данных. 
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП."""

global data_storage

print('Проект "Склад оргтехники"')


class Warehouse:
    """Класс "Склад" имеет методы: Добавления на остатки; Списание в подразделение; Валидация вводимых данных"""
    # словарь для хранения данных склада
    data_storage = {}
    # подстановочные знаки для пользовательсвого интерфейса
    item_sign = {'P': 'PRINTER', 'S': 'SCANNER', 'C': 'COPIER'}

    def __init__(self):
        pass

    @staticmethod
    def add_to_warehouse():
        """Диалог приёмки оргтехники на склад."""
        print('\nДобавляем оборудование на склад.')
        # Выбираем позицию
        item_to_add = Warehouse.choose_equip()
        while True:
            try:
                how_much = int(input(f'\nКакое количество {Warehouse.item_sign.get(item_to_add)} добавить? '))
            except ValueError:
                print('\nОШИБКА! При указании количества допустимы только цифры!')
            else:
                # если заданы адекватные параметры выполняет добавление
                Warehouse.add_to_stock(Warehouse.item_sign.get(item_to_add), how_much)
                # отчет о выполненной операции
                print(f'\nПополнение склада выполнено.\nНаименование: '
                      f'{Warehouse.item_sign.get(item_to_add)}\nКоличество: {how_much}\n ')
                break
        # текущий статус склада
        print('Текущее состояние склада после пополнения:')
        Warehouse.show_warehouse_status()
        one_more_item = (
            input('Требуется ли добавить еще оборудование? Y/N: ')).upper()
        if one_more_item == 'Y':
            Warehouse.add_to_warehouse()
        else:
            menu()

    @staticmethod
    def add_to_stock(add_item_name, add_number):
        """Обработчик добавления оборудования на склад.
        Если наименование отсутствует в data_storage - добавляет его в список,
        если имеется в списке - изменяет его количество."""
        if add_number <= 0:
            print('Нечего добавить, количество 0 или отрицательное.')
        elif Warehouse.data_storage.get(add_item_name):
            Warehouse.data_storage.update({add_item_name: (Warehouse.data_storage.get(add_item_name) + add_number)})
        else:
            Warehouse.data_storage.update({add_item_name: add_number})

    @staticmethod
    def out_item():
        """Диалог передачи со склада в подразделение."""
        # отображает текущий статус склада для информации
        print('Передаем в подразделение.\nТекущее состояние склада:')
        Warehouse.show_warehouse_status()
        # выбор оборудования для передачи в подразделение
        item_to_give = Warehouse.choose_equip()
        while item_to_give not in Warehouse.data_storage or Warehouse.data_storage.get(
                Warehouse.item_sign.get(item_to_give)) == 0:
            # проверка наличия выбранного оборудования на складе
            if Warehouse.item_sign.get(item_to_give) not in Warehouse.data_storage or Warehouse.data_storage.get(
                    Warehouse.item_sign.get(item_to_give)) == 0:
                print(
                    '\nНа складе запрошенное оборудование отсутствует***\n')
                item_to_give = Warehouse.choose_equip()
            else:
                break
        while True:
            try:
                how_much = int(
                    input(f'\nНа складе имеется {Warehouse.data_storage.get(Warehouse.item_sign.get(item_to_give))} '
                          f'{Warehouse.item_sign.get(item_to_give)}. Какое количество передаем? '))
            except ValueError:
                print('\nОШИБКА! При указании количества допустимы только цифры!')
                # continue
            else:
                # проверка на указание отрицательного количества или больше чем в наличии
                if how_much <= 0 or how_much > Warehouse.data_storage.get(Warehouse.item_sign.get(item_to_give)):
                    print('\nЗадано некорректное количество для передачи!')
                    Warehouse.out_item()  # укаазано неадекватное количество, возврат к началу процесса передачи
                # запрос наименования подразделения куда передаем оборудование
                department = input('\nВ какое подразделение передаём? ')
                # передача в подразделение, изменяет количество позиции в data_storage
                Warehouse.data_storage.update(
                    {Warehouse.item_sign.get(item_to_give):
                         (Warehouse.data_storage.get(Warehouse.item_sign.get(item_to_give)) - how_much)}
                )
                # отчет о выполненной операции
                print(
                    f'\nВ "{department}" передано {how_much} {Warehouse.item_sign.get(item_to_give)}, '
                    f'на складе осталось {Warehouse.data_storage.get(Warehouse.item_sign.get(item_to_give))} '
                    f'{Warehouse.item_sign.get(item_to_give)}'
                )
            one_more_item = (input('Требуется ли еще передать оборудование? Y/N: ')).upper()
            if one_more_item == 'Y':
                Warehouse.out_item()
            else:
                menu()

    @staticmethod
    def choose_equip():
        """Обработчик корректности выбора типа оборудования"""
        while True:
            try:
                item_to_give = (input(f'\nКакой тип оборудования?\nВыберите соответствующий знак в скобках:\n'
                                      f'Printer (P), Scanner (S) или Copier (С)? ')).upper()
                if item_to_give != 'P' and item_to_give != 'S' and item_to_give != 'C':
                    raise WrongInput
                elif item_to_give == 'Q':  # quit (выход из программы)
                    exit()
            except WrongInput as wi:
                print(wi, 'Необходимо выбирать из предложенных вариантов.')
            else:
                return item_to_give

    @staticmethod
    def show_warehouse_status():
        """Отчет о текущих остатках на складе"""
        if len(Warehouse.data_storage) == 0:
            print('На складе ничего нет. Добавьте что-нибудь прежде передачи в подразделение.')
            Warehouse.add_to_warehouse()
        else:
            for _ in Warehouse.data_storage.items():
                print(_[0], _[1], sep=' - ')


class OfficeEquipment:
    """Базовый класс «Оргтехника», для классов-наследников - конкретные типы оргтехники (принтер, сканер, ксерокс).
    В базовом классе определены параметры, общие для приведённых типов.
    В классах-наследниках реализованы параметры, уникальные для каждого типа оргтехники. """

    def __init__(self, name, page):
        self.page = page  # some text to print
        self.name = name  # unique name of example

    def make_image(self):  # get self.page and make image (color_hard_copy, picture_file, greyscale_hard_copy)
        return 'Some copy done'

    def on(self):  # change status On/Off to On
        return f'{self} включился'

    def off(self):  # change status On/Off to Off
        return f'{self} выключился'

    @staticmethod
    def driver(arg):
        """Запускает работу обрудования выбранного в меню"""
        # перчать на принтере
        if arg == 'p':
            print(f'\nВыбран вывод страницы на печать\n', Printer.on(printer))
            print(Printer.make_image(printer))
            print(Printer.off(printer))
        # сканирование в файл
        elif arg == 's':
            print(f'\nВыбрано сканирование страницы\n', Scanner.on(scanner))
            print(Scanner.make_image(scanner))
            print(Scanner.off(scanner))
        # изготовление копий
        if arg == 'c':
            print(f'\nВыбрано изготовление копий\n', Copier.on(copier))
            print(Copier.make_image(copier))
            print(Copier.off(copier))


"""Классы наследники"""


class Printer(OfficeEquipment):
    def __init__(self, color: bool, page, name):
        super().__init__(name, page)
        self.color = color  # color printing ability: True/False
        self.name = name  # the name for example

    def __str__(self):
        return f'{self.name}'

    def make_image(self):
        return f'{"Цветная копия" if self.color else "Копия в шкале серого"} ' \
               f'"{self.page}" распечатана на принтере {self.name}'


class Scanner(OfficeEquipment):
    def __init__(self, resolution: int, page, name):
        super().__init__(name, page)
        self.resolution = resolution

    def __str__(self):
        return f'{self.name}'

    def make_image(self):
        return f'"Электронная копия {self.page}" с разрешением ' \
               f'{self.resolution} dpi сохранена в файл со сканера {self.name}'


class Copier(OfficeEquipment):
    def __init__(self, quantity: int, page, name):
        super().__init__(name, page)
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}'

    def make_image(self):
        return f'{self.quantity} копий {self.page} сделано на копире {self.name}'


printer = Printer(True, 'текста для печати', 'Printy')
# print(Printer.on(printer))
# print(Printer.make_image(printer))
# print(Printer.off(printer))

scanner = Scanner(400, 'страницы для сканирования', 'Scany')
# print(Scanner.on(scanner))
# print(Scanner.make_image(scanner))
# print(Scanner.off(scanner))

copier = Copier(5, 'листовки', 'Xerox')


# print(Copier.on(copier))
# print(Copier.make_image(copier))
# print(Copier.off(copier))


class WrongInput(Exception):
    """Обработка исключений при работе с классом склада и меню"""
    def __init__(self):
        pass

    def __str__(self):
        self.txt = '\nОШИБКА! Некорректный ввод.'
        return self.txt


# 1 с чем будем работать? склад/оборудование?
# 2 вывести одно из меню в зависимости от того что выбрано
# 3 передать управление в соответствующий класс
def menu():
    warehouse_menu_text = f'ВВЕДИТЕ |           ДЛЯ ДЕЙСТВИЯ\n' \
                          f'{("-" * 10) + "|" + ("-" * 52)} \n' \
                          f'{(" " * 22)}"С К Л А Д"\n' \
                          '     A    | - добавить оборудование на склад (add)\n' \
                          '     M    | - передать оборудование в подразделение (move)\n' \
                          '     R    | - посмотреть остатки (stock)\n' \
                          '     Q    | - выйти из программы (quit)Q\n'

    equipment_menu_text = f'{(" " * 16)}"О Б О Р У Д О В А Н И Е"\n' \
                          f'ВВЕДИТЕ |           ДЛЯ ДЕЙСТВИЯ\n' \
                          f'{("-" * 10) + "|" + ("-" * 52)} \n' \
                          '     P    | - вывести страницу на перчать (print)\n' \
                          '     S    | - сканировать страницу (scan)\n' \
                          '     C    | - сделать копию (copy)' \
                          '     Q    | - выйти из программы (quit)Q\n'

    mode = (input('\nС чем будем работать?\nСо складом (W), С оборудованием (E)')).upper()
    while True:
        try:
            if mode != 'W' and mode != 'E':
                raise WrongInput
            elif mode == 'W':
                print('\nДля продолжения выбирите действие.\n\n', warehouse_menu_text)
                break
            elif mode == 'E':
                print('\nДля продолжения выбирите действие.\n\n', equipment_menu_text)
                break
        except WrongInput as wi:
            print(wi, 'Только предложенные варианты допустимы.')
            menu()

    # при выборе склада
    while True:  # работаем пока пользователь не наберет Q
        if mode == 'W':
            try:
                do = (input('\nВыбирите действие: ')).upper()
                if do == 'Q':  # quit (выход из программы)
                    exit()
                elif do == 'A':  # add
                    """добавить оборудование в сток"""
                    Warehouse.add_to_warehouse()
                elif do == 'M':  # move
                    """передать оборудование в подразделение"""
                    Warehouse.out_item()
                elif do == 'R':
                    """посмотреть остатки склада"""
                    Warehouse.show_warehouse_status()
                else:
                    raise WrongInput
            except WrongInput as wi:
                print(wi, 'Нужно выбрать из предложенных вариантов')
        # при выборе оборудования
        elif mode == 'E':
            try:
                do = (input('\nВыбирите действие: ')).upper()
                if do == 'P':
                    """напечатать документ"""
                    OfficeEquipment.driver('p')
                elif do == 'S':
                    """сканировать документ"""
                    OfficeEquipment.driver('s')
                elif do == 'C':
                    """сделать копию документа"""
                    OfficeEquipment.driver('c')
                elif do == 'HELP':
                    print(warehouse_menu_text, equipment_menu_text)
                else:
                    raise WrongInput
            except WrongInput as wi:
                print(wi, 'Нужно выбрать из предложенных вариантов')


menu()  # запуск программы
