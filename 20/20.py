#!python3

import sys
from operator import add

def main():
    with open('20.txt', 'r') as f, open('20_out.txt', 'w') as f_out:
        lines = f.readlines()

        positions = {}
        velocities = {}
        accelerations = {}

        for i, line in enumerate(lines):
            p, v, a = [[int(n) for n in vector[3:-1].split(',')] for vector in line.strip().split(', ')]
            positions[i] = p
            velocities[i] = v
            accelerations[i] = a

        # Part 1
        smallest = i
        smallest_sum = sys.maxsize
        for i, a in accelerations.items():
            s = sum([abs(n) for n in a])
            if s < smallest_sum:
                smallest = i
                smallest_sum = s

        print(smallest)
        print(smallest, file=f_out)

        # Part 2
        # I'm sure there'll be no more collisions after 100 ticks, right?
        for tick in range(100):
            reverse_positions = {}
            for i, p in list(positions.items()):
                p = tuple(p)
                if p in reverse_positions:
                    reverse_positions[p].append(i)
                else:
                    reverse_positions[p] = [i]

            for p, items in reverse_positions.items():
                if len(items) > 1:
                    for i in items:
                        positions.pop(i)
                        velocities.pop(i)
                        accelerations.pop(i)

            for i, a in accelerations.items():
                velocities[i] = list(map(add, velocities[i], a))
                positions[i] = list(map(add, positions[i], velocities[i]))

        answer = len(positions)
        print(answer)
        print(answer, file=f_out)


if __name__ == '__main__':
    main()
