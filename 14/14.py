#!python3

import operator
import itertools
from functools import reduce


def main():
    with open('14_out.txt', 'w') as f_out:
        # Puzzle input
        in_str = 'ffayrhll'

        grid = []
        for i in range(128):
            key = f'{in_str}-{i}'
            hash_str = knot_hash(key)
            binary = ''.join(['{:0>4b}'.format(int(c, 16)) for c in hash_str])
            grid.append(binary)

        # Part 1
        used = sum([sum([1 if c == '1' else 0 for c in row]) for row in grid])
        print(used)
        print(used, file=f_out)

        # Part 2
        regions = 0
        seen = set()
        for i in range(128):
            for j in range(128):
                if (i, j) in seen:
                    continue
                if grid[i][j] != '1':
                    continue
                regions += 1
                q = [(i, j)]
                while len(q) > 0:
                    curr = q.pop()
                    seen.add(curr)
                    for point in neighbors(*curr):
                        x, y = point
                        if point in seen:
                            continue
                        if x < 0 or x >= 128 or y < 0 or y >= 128:
                            continue
                        if grid[x][y] != '1':
                            continue
                        q.append(point)
        print(regions)
        print(regions, file=f_out)


def neighbors(x, y):
    yield (x + 1, y)
    yield (x, y + 1)
    yield (x - 1, y)
    yield (x, y - 1)


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
                continuRe
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
