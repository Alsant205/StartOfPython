"""Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк
и сохраните в переменные, выведите на экран. """
number = 5
string = '"какой-то текст"'

print('Переменная с числом =', number, 'Переменная со строкой =', string)
print()

user_number1 = input("Введите число: ")
user_number2 = input("Введите еще одно число: ")

user_string1 = input('Введите слово или фразу: ')
user_string2 = input('Введите еще слово или фразу: ')

print('Вы ввели:', 'Первое число -', user_number1, '   Второе число -', user_number2,
      '   Певую строку -', user_string1, '   Вторую строку -', user_string2)
