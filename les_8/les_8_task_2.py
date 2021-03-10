# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.

import heapq
from collections import Counter
from collections import namedtuple


class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    return code


def huffman_decode(encoded, code):
    sx = []
    enc_ch = ''
    for ch in encoded:
        enc_ch += ch
        for dec_ch in code:
            if code.get(dec_ch) == enc_ch:
                sx.append(dec_ch)
                enc_ch = ''
                break
    return ''.join(sx)


def main():
    s = input('Введите строку, которую необходимо закодировать: ')
    code = huffman_encode(s)
    encoded = ''.join(code[ch] for ch in s)
    print(f'В строке {len(code)} уникальных символов, каждому символу соответствует код: ')
    for ch in sorted(code):
        print(f"'{ch}' - {code[ch]}")
    print(f'Закодированная строка, длиной {len(encoded)} знаков: {encoded}.')
    print(f'Декодирование: {huffman_decode(encoded, code)}')


main()

"""
Введите строку, которую необходимо закодировать: ad astra per aspera
В строке 8 уникальных символов, каждому символу соответствует код: 
' ' - 110
'a' - 10
'd' - 0110
'e' - 010
'p' - 001
'r' - 111
's' - 000
't' - 0111
Закодированная строка, длиной 54 знаков: 100110110100000111111101100010101111101000000101011110.
Декодирование: ad astra per aspera
"""