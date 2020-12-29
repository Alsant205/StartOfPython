# from sys import argv
#
# script_name, param_1, param_2, param_3 = argv  # библиатаека argv хранит список передаваемых параметров
#
# # первый параметр это всегда путь к исполняемому файлу скрипта. Его при выполнении нужно будет как-то обходить.
# # убирать, складывать, вырезать и т.п.
#
# print("Имя скрипта: ", script_name)
# print("Параметр 1: ", param_1)
# print("Параметр 2: ", param_2)
# print("Параметр 3: ", param_3)
#
# # 1 способ передачи параметров с помощью РС
# # Меню RUN > EDIT CONFIGURATIONS > Parameters
# # заполняем в поле через пробел значения параметров, при этом параметры преобразуются в строки
#
# # 2 способ передачи параметров с помощью Terminal
# # находясь в директории с файлом скрипта набираем python [имя файла скрипта с расширением] и параметры через пробел
#
# # 3 способ передачи параметров с помощью командной строки
# # находясь в директории с файлом скрипта набираем python [имя файла скрипта с расширением] и параметры через пробел

# l = 'indivisibility'
# l = list(l)
# a = 0
# for i in l:
#     if l.count(i) > 2:
#         a += 1
# # print(a)
#
#
# def duplicate_count(text):
#     l = list(text)
#     a = []
#     a = [i for i in l if l.count(i) > 1]
#     for i in a:
#
#     return

# duplicate_count('kjdbcdkdh')


stro = 'fhgn nvhf Nhh kjj Nh  YYGv hjjb'

b = (stro.lower()).split()

# print(s)


def int_func(a):
    # n = a.title()
    return a.title()

c = []
for word in b:  # перебираем слова и отправляем в функцию
    c.append(int_func(word))
print(c)


