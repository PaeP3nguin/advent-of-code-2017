#!python3

import math
from collections import defaultdict

def main():
    with open('3_out.txt', 'w') as f_out:
        # Part 1
        square = 289326

        side_len = math.ceil(math.sqrt(square))
        if side_len % 2 == 0:
            side_len += 1

        # Figure which layer of the spiral our number is at
        circumference = (side_len - 1) // 2

        # Number in the bottom right of the layer
        layer_max = side_len ** 2

        # Distance from edge of spiral
        position = (layer_max - square) % (side_len - 1)

        steps = circumference + abs(position - circumference)

        print(steps)
        print(steps, file=f_out)

        # Part 2
        grid = defaultdict(dict)
        grid[0] = {0: 1}
        for x, y in spiral():
            sum_adjacent = 0
            for a, b in adjacent(x, y):
                adj_col = grid[a]
                if b in adj_col:
                    sum_adjacent += adj_col[b]
            if sum_adjacent > square:
                print(sum_adjacent)
                print(sum_adjacent, file=f_out)
                break
            col = grid[x]
            col[y] = sum_adjacent
            grid[x] = col


def spiral():
    circumference = 1
    while True:
        for x, y in spiral_layer(circumference, 0, 0):
            yield (x, y)
        circumference += 1

def spiral_layer(circumference, init_x, init_y):
    for y in range(-circumference + 1, circumference + 1):
        yield (init_x + circumference, init_y + y)
    for x in range(circumference - 1, -circumference - 1, -1):
        yield (init_x + x, init_y + circumference)
    for y in range(circumference - 1, -circumference - 1, -1):
        yield (init_x - circumference, init_y + y)
    for x in range(-circumference + 1, circumference + 1):
        yield (init_x + x, init_y - circumference)

def adjacent(init_x, init_y):
    for x, y in spiral_layer(1, init_x, init_y):
        yield (x, y)

if __name__ == '__main__':
    main()
