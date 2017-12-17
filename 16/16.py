#!python3

def main():
    with open('16.txt', 'r') as f, open('16_out.txt', 'w') as f_out:
        line = f.readline()
        dance_moves = line.strip().split(',')

        letters = [chr(c) for c in range(97, 113)]

        # Part 1
        programs = letters.copy()
        # programs = ['a', 'b', 'c', 'd', 'e']
        # dance_moves = ['s1', 'x3/4', 'pe/b']
        for move in dance_moves:
            if move[0] == 's':
                spin_size = int(move[1:])
                programs = programs[-spin_size:] + programs[:len(programs) - spin_size]
            elif move[0] == 'x':
                a, b = [int(n) for n in move[1:].split('/')]
                programs[a], programs[b] = programs[b], programs[a]
            elif move[0] == 'p':
                swap_a, swap_b = move[1], move[3]
                a, b = programs.index(swap_a), programs.index(swap_b)
                programs[a], programs[b] = programs[b], programs[a]
        print(''.join(programs))
        print(''.join(programs), file=f_out)

        # Part 2
        seen = set()
        cycle_len = 0
        programs = letters.copy()
        for i in range(1000000000):
            programs_str = ''.join(programs)
            if programs_str in seen:
                cycle_len = i
                break
            seen.add(programs_str)
            for move in dance_moves:
                if move[0] == 's':
                    spin_size = int(move[1:])
                    programs = programs[-spin_size:] + programs[:len(programs) - spin_size]
                elif move[0] == 'x':
                    a, b = [int(n) for n in move[1:].split('/')]
                    programs[a], programs[b] = programs[b], programs[a]
                elif move[0] == 'p':
                    swap_a, swap_b = move[1], move[3]
                    a, b = programs.index(swap_a), programs.index(swap_b)
                    programs[a], programs[b] = programs[b], programs[a]
        print(f'Cycle length: {cycle_len}')

        # Sure I mean I guess I could do a better job but hey, copy pasta is easy
        programs = letters.copy()
        for i in range(1000000000 % cycle_len):
            for move in dance_moves:
                if move[0] == 's':
                    spin_size = int(move[1:])
                    programs = programs[-spin_size:] + programs[:len(programs) - spin_size]
                elif move[0] == 'x':
                    a, b = [int(n) for n in move[1:].split('/')]
                    programs[a], programs[b] = programs[b], programs[a]
                elif move[0] == 'p':
                    swap_a, swap_b = move[1], move[3]
                    a, b = programs.index(swap_a), programs.index(swap_b)
                    programs[a], programs[b] = programs[b], programs[a]
        print(''.join(programs))
        print(''.join(programs), file=f_out)


if __name__ == '__main__':
    main()
