#!python3

def main():
    with open('12.txt', 'r') as f, open('12_out.txt', 'w') as f_out:
        lines = f.readlines()

        connections = {}
        for line in lines:
            program, adjacent = line.strip().split(' <-> ')
            adjacent = adjacent.split(', ')
            if program not in connections:
                connections[program] = []
            for c in adjacent:
                if c not in connections:
                    connections[c] = []
                connections[c].append(program)
                connections[program].append(c)

        # Part 1
        q = ['0']
        seen = set()
        while len(q) > 0:
            program = q.pop()
            seen.add(program)
            for adjacent in connections[program]:
                if adjacent not in seen:
                    q.append(adjacent)
        answer = len(seen)
        print(answer)
        print(answer, file=f_out)

        groups = 0
        seen = set()
        for program in connections.keys():
            if program in seen:
                continue
            groups += 1
            q = [program]
            while len(q) > 0:
                p = q.pop()
                seen.add(p)
                for adjacent in connections[p]:
                    if adjacent not in seen:
                        q.append(adjacent)
        # Part 2
        print(groups)
        print(groups, file=f_out)


if __name__ == '__main__':
    main()
