#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
from sys import argv

try:
    script_name, amount_in_hour, hour_rate, bonus = argv
except ValueError:
    print('\nВы ввели недостаточно арументов!'.upper())

if len(argv) != 4:
    print(f'Введено значений {len(argv) - 1}, необходимо 3. Введите значения через пробел:\n1. Количество '
          f'отработанных часов\n2. Размер оплаты за час\n3. Размер премии\n')
else:
    try:
        salary = (int(amount_in_hour) * int(hour_rate)) + int(bonus)
        print(f'1. Количество отработанных часов - {amount_in_hour} ч.\n'
              f'2. Размер оплаты за час - {hour_rate} руб.\n'
              f'3. Размер премии - {bonus} руб.\n'
              f'Зарплата составит = {salary} руб.\n')
    except ValueError:
        print('Необходимо водить цифры.'.upper())
