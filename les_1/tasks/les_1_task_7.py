# 7. Определить, является ли год, который ввел пользователь, високосным или не високосным.

year = int(input('Введите год: '))
if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    print('Невисокосный год')
else:
    print('Високосный год')