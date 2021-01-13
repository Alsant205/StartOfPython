"""Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict."""

mode = input('Какой способ реализации запустить? Введите list или dict')

if mode == 'list':
    """реализация через list"""

    print(f'\n{("*" * 20)} Реализация через list {("*" * 20)}')

    winter = [12, 1, 2]
    spring = [3, 4, 5]
    summer = [6, 7, 8]
    autumn = [9, 10, 11]

    while True:
        month_num = input('\nВведите месяц в виде целого числа от 1 до 12: ')
        if month_num.isdigit and 1 <= int(month_num) <= 12:  # проверяем что введено верное число
            if winter.count(int(month_num)) != 0:
                print('Указанный месяц относится к Зиме')
                break
            elif spring.count(int(month_num)) != 0:
                print('Указанный месяц относится к Весне')
                break
            elif summer.count(int(month_num)) != 0:
                print('Указанный месяц относится к Лету')
                break
            else:
                print('Указанный месяц относится к Осени')
        else:
            print('Вы ошиблись с вводом. Попробуйте еще раз. ')

else:
    """реализация через dict"""

    print(f'\n{("*" * 20)} Реализация через dict {("*" * 20)}')
    year = {
        'winter': {12: 'Декабрь', 1: 'Январь', 2: 'Февраль'},
        'spring': {3: 'Март', 4: 'Апрель', 5: 'Май'},
        'summer': {6: 'Июнь', 7: 'Июль', 8: 'Август'},
        'autumn': {9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь'}
    }

    while True:
        month_num = input('\nВведите месяц в виде целого числа от 1 до 12: ')
        if 1 <= int(month_num) <= 12:  # проверяем что введено верное число
            for season in year:
                year.get(season)
                month = year.get(season).get(int(month_num))

                if season == 'winter' and month is not None and month == 'Декабрь' or month == 'Январь' or month == 'Февраль':
                    print(f'Указанный месяц {month} относится к Зиме')
                    break
                elif season == 'spring' and month is not None and month == 'Март' or month == 'Апрель' or month == 'Май':
                    print(f'Указанный месяц {month} относится к Весне')
                    break
                elif season == 'summer' and month is not None and month == 'Июнь' or month == 'Июль' or month == 'Август':
                    print(f'Указанный месяц {month} относится к Лету')
                    break
                elif season == 'autumn' and month is not None and month == 'Сентябрь' or month == 'Октябрь' or month == 'Ноябрь':
                    print(f'Указанный месяц {month} относится к Осени')
                    break
            break
        else:
            print('Вы ошиблись с вводом. Попробуйте еще раз. ')
