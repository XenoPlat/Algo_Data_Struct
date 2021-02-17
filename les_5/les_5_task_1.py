# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за 4 квартала для каждого предприятия. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше
# среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import namedtuple
from statistics import mean

New_Company = namedtuple('New_Company', 'name profit_list avg')

lst = []
for i in range(int(input('Введите количество компаний: '))):
    arg = input('Введите построчно имя компании и поквартальную прибыль, через пробел:\n').split()
    lst.append(New_Company(arg[0], arg[1:], mean(map(int, arg[1:3]))))

avg = mean([i.avg for i in lst])

print('_' * 70, '\n')

for i in lst:
    print(f'Компания: {i.name} \t\tСредняя прибыль за год: {i.avg}')

print('_' * 70, '\n')

print('Средняя прибыль по всем компаниям за год: ', avg)

print('_' * 70, '\n')

print('Компании с прибылью меньше средней:')
for i in lst:
    if i.avg < avg:
        print(i.name,':',i.avg)

print('Компании с прибылью больше средней:')
for i in lst:
    if i.avg > avg:
        print(i.name,':',i.avg)