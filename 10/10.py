#!python3

import operator
import itertools
from functools import reduce

def main():
    with open('10.txt', 'r') as f, open('10_out.txt', 'w') as f_out:
        line = f.readline()
        lengths = [int(n) for n in line.split(',')]

        # Part 1
        circle_size = 256
        circle = list(range(0, circle_size))
        position = 0
        skip_size = 0
        for length in lengths:
            if length == 0:
                position = (position + length + skip_size) % circle_size
                skip_size += 1
                continue
            for i, j in zip(range(position, position + length // 2), range(position + length - 1, position - 1, -1)):
                i %= circle_size
                j %= circle_size
                circle[i], circle[j] = circle[j], circle[i]
            position = (position + length + skip_size) % circle_size
            skip_size += 1
        answer = circle[0] * circle[1]
        print(answer)
        print(answer, file=f_out)

        # Part 2
        final_hash = knot_hash(line.strip())
        print(final_hash)
        print(final_hash, file=f_out)


def knot_hash(in_str):
    suffix = [17, 31, 73, 47, 23]
    lengths = [ord(c) for c in in_str] + suffix
    circle_size = 256
    circle = list(range(0, circle_size))
    position = 0
    skip_size = 0
    for i in range(64):
        for length in lengths:
            if length == 0:
                position = (position + length + skip_size) % circle_size
                skip_size += 1
                continue
            for i, j in zip(range(position, position + length // 2), range(position + length - 1, position - 1, -1)):
                i %= circle_size
                j %= circle_size
                circle[i], circle[j] = circle[j], circle[i]
            position = (position + length + skip_size) % circle_size
            skip_size += 1

    dense_hash = []
    for group in grouper(16, circle):
        dense_hash.append(reduce(operator.xor, group))

    return ''.join(['{:0>2x}'.format(n) for n in dense_hash])


def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)


if __name__ == '__main__':
    main()
