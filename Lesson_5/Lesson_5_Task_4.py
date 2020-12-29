import re

"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл. """

# with open('eng_count.txt', 'r') as en_file:
#     en_ru_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре'}
#     full_fill = []
#     for el in en_file:
#         for key in en_ru_dict:
#             if key.capitalize() in el:
#                 el = el.replace(key.capitalize(), (en_ru_dict.get(key).capitalize()))
#                 full_fill.append(el)
#
# with open('ru_count.txt', 'w', encoding='utf-8') as ru_file:
#     if ru_file.tell() > 0:
#         ru_file.seek(0)
#     ru_file.write(''.join(full_fill))


# ----------------------------------- вариант решения с библиотекой re----------------------------------------------

with open('text_4.txt', 'r') as en_file:
    en_ru_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре'}
    full_fill = []
    content = ''.join(en_file.readlines())
    for key in en_ru_dict:
        content = re.sub(key.capitalize(), (en_ru_dict.get(key).capitalize()), content)
    full_fill.append(content)

with open('ru_count.txt', 'w', encoding='utf-8') as ru_file:
    if ru_file.tell() > 0:
        ru_file.seek(0)
    ru_file.write(' '.join(full_fill))
