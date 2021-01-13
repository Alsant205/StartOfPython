"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

with open('text.txt', 'w', encoding='utf-8') as t_file:
    string = None
    while string != '':
        string = input('Введите запись и нажмите Enter. Для завершения ввода оставьте строку пустой и нажмите Enter.\n')
        if string != '':
            t_file.write(string + '\n')

with open('text.txt', 'r') as t_file:
    str_number = 0
    a = []
    for num, line in enumerate(t_file, 1):
        str_number += 1
        a.append(f'Строка {num} "{line[:-1]}", слов - {line.count(" ") + 1}.\n')
    print(f'В файле {t_file.name} строк - {str_number}.\n{"".join(a)}')
