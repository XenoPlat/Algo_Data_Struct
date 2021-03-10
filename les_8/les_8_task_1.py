# 1. Определение количества различных подстрок с использованием хеш-функции.

import hashlib

usr_str = str(input("Введите строку из строчных латинских букв: ").lower())

print(f'Строка {usr_str} имеет длину {len(usr_str)} сиволов.')

subs_set = set()

for i in range(len(usr_str)):
    for j in range(len(usr_str) - 1 if i == 0 else len(usr_str), i, -1):
        subs_set.add(hashlib.sha1(usr_str[i:j].encode('utf-8')).hexdigest())

print("Количество различных подстрок в этой строке:", len(subs_set))

'''
Введите строку из строчных латинских букв: GeekBrains University
Строка geekbrains university имеет длину 21 сиволов.
Количество различных подстрок в этой строке: 223

'''