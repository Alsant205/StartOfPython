"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней
величины дохода сотрудников. """

with open('text_3.txt', 'r') as s_file:
    string = s_file.readlines()  # считываем все строки из файла
    average = 0  # для целей подсчета среднего оклада
    head_count = 0  # считаем количество сотрудников
    for data in string:  # получаем элемент списка как строку записи о сотруднике
        head_count += 1
        data = data.split()  # делим строку на элементы нового списка
        average += float(data[-1])
        if float(data[-1]) < 20000:  # определяем оклады соответствующие условию задачи
            print(f'{data[0]} имеет оклад менее 20 тыс. и составляет {data[1]}')  # выводим фамилию сотрудника если Истина
    print(f'Средний оклад составляет - {average / head_count:.2f}')
