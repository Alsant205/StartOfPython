"""Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text """


def int_func(arg):
    """проверяет набрано ли слово латиницей и в таком случае возвращает True"""
    arg = tuple(arg)  # разбиваем слово на буквы для проверки по условию "только маленькие английские"
    for letter in arg:  # последовательно получаем каждую букву из слова
        if 97 <= ord(letter) <= 122:  # проверяем попадает ли буква в диапазон
            continue  # переходим к проверке следующей буквы
        else:
            return False  # если наткнулись не неверный символ, возвращаем для слова False
    return True  # если слово прошло проверку


"""Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово 
состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с 
заглавной буквы. Необходимо использовать написанную ранее функцию int_func(). """

source_string = input('Введите слова разделенные пробелом набранные маленькими латинскими буквами:\n')
#  строка для проверки
# nice авп ъghj jапро hjjпаро вапрghgh cool

source_string = source_string.split()  # разделим строку на слова для проверки каждого слова
new_string = []  # сюда будем записывать слова прошедшие проверку

for word in source_string:  # перебираем слова и отправляем на проверку в функцию
    if int_func(word):
        new_string.append(str(word).capitalize())  # увеличиваем первую букву и добавляем с список

print('Обработанная строка: ', ' '.join(new_string))
