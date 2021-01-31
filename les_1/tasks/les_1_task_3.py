# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random as rd

select = input('[1] - Целое число\n'
               '[2] - Вещественное число\n'
               '[3] - Символ\n'
               'Выберите тип: ')
if select not in ['1', '2', '3']:
    print('Ошибка выбора типа')
    exit()

print('Выберите диапозон чисел или символов')
start = input('От: ')
stop = input('До: ')

if select == '1':
    print(f'Ваш результат: {rd.randint(int(start), int(stop))}')
elif select == '2':
    print(f'Ваш результат: {rd.uniform(float(start), float(stop)):.3}')
elif select == '3':
    print(f'Ваш результат: {chr(rd.randint(ord(start), ord(stop)))}')