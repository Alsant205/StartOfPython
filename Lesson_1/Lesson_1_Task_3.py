"""Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369."""

# number = int(input('введите число: '))
#
# result = number + number * 11 + number * 111
#
# print(f'{number} + {number * 11} + {number * 111}')
#
#
# print(result)

number = input('введите число: ')  # получаем число в виде строки

# внутри скобок удваиваем и утраиваем строку согласно условий задачи,
# а затем преобразуем эти строки в числа и выполняем их сложение
result = int(number) + int(number * 2) + int(number * 3)

print(f'{number} + {number * 2} + {number * 3}')  # Для наглядности процесса вычисления

print(result)