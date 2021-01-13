import re
from random import randint
from functools import reduce

# lst = ['1', '2', '3']
#
# shadule = {re.findall('[А-я]{4,}', i)[0]: sum + int(re.findall('\d+'.strip(), i)[k]) for i in lst for k in
#            range(len(re.findall('\d+'.strip(), i)))}
#
# print(shadule)

"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа 
должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open('rand_sum.txt', 'w', encoding='utf-8') as random_file:
    rand_list = [str(randint(1, 101)) for rand_el in range(10)]  # генератор
    random_file.write(' '.join(rand_list))  # записываем строку с пробелами согласно условиям задачи

with open('rand_sum.txt', 'r', encoding='utf-8') as random_file:
    summ = 0
    a = (random_file.readline()).split()
    for el in a:
        summ = summ + int(el)
    print(f'Сумма чисел {", ".join(a)} равняется {summ}')


# посмотреть как можно сделать с помощью reduce
