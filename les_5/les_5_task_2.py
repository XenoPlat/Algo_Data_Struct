# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число
# представляется как массив, элементы которого — цифры числа. Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера:
# [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

hex_symb = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')

def hex_dec(num):
    return sum([hex_symb.index(v) * 16 ** idx for idx, v in enumerate(num)])

def dec_hex(num):
    result = deque()
    while num != 0:
        result.appendleft(hex_symb[num % 16])
        num = num // 16
    return result

a16 = list(input('Введите первое число: ').upper())
b16 = list(input('Введите второе число: ').upper())

a16.reverse()
b16.reverse()
a10 = hex_dec(a16)
b10 = hex_dec(b16)

ab_sum10 = a10 + b10
ab_prod10 = a10 * b10

print(f'Сумма: {dec_hex(ab_sum10)}')
print(f'Произведение: {dec_hex(ab_prod10)}')