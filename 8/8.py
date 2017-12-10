#!python3

import sys
from collections import defaultdict


def main():
    with open('8.txt', 'r') as f, open('8_out.txt', 'w') as f_out:
        lines = f.readlines()

        # Part 1
        registers = defaultdict(int)
        for line in lines:
            reg, op, n, _, cond_reg, cond, m = line.split()
            cond_reg_val = registers[cond_reg]
            if not eval(f'cond_reg_val {cond} {m}'):
                continue
            if op == 'inc':
                registers[reg] += int(n)
            elif op == 'dec':
                registers[reg] -= int(n)
        max_val = max(registers.values())
        print(max_val)
        print(max_val, file=f_out)

        # Part 2
        registers = defaultdict(int)
        max_val = -sys.maxsize
        for line in lines:
            reg, op, n, _, cond_reg, cond, m = line.split()
            cond_reg_val = registers[cond_reg]
            if not eval(f'cond_reg_val {cond} {m}'):
                continue
            if op == 'inc':
                registers[reg] += int(n)
            elif op == 'dec':
                registers[reg] -= int(n)
            if registers[reg] > max_val:
                max_val = registers[reg]
        print(max_val)
        print(max_val, file=f_out)


if __name__ == '__main__':
    main()
