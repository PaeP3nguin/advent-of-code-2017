#!python3


def main():
    with open('5.txt', 'r') as f, open('5_out.txt', 'w') as f_out:
        lines = f.readlines()

        # Part 1
        instructions = [int(n) for n in lines]
        instruction_count = len(instructions)
        steps = 0
        ip = 0
        while ip >= 0 and ip < instruction_count:
            curr = instructions[ip]
            instructions[ip] += 1
            ip += curr
            steps += 1
        print(steps)
        print(steps, file=f_out)

        # Part 2
        instructions = [int(n) for n in lines]
        steps = 0
        ip = 0
        while ip >= 0 and ip < instruction_count:
            curr = instructions[ip]
            if curr >= 3:
                instructions[ip] -= 1
            else:
                instructions[ip] += 1
            ip += curr
            steps += 1
        print(steps)
        print(steps, file=f_out)


if __name__ == '__main__':
    main()
