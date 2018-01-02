#!python3

from operator import add

def main():
    with open('19.txt', 'r') as f, open('19_out.txt', 'w') as f_out:
        lines = [l[:-1] for l in f.readlines()]
        rows = len(lines)

        curr = '|'
        curr_pos = (0, lines[0].index('|'))
        direction = (1, 0)
        letters = []

        # Part 2
        steps = 1

        while True:
            r, c = map(add, curr_pos, direction)
            next_char = lines[r][c]
            if next_char == '+':
                if direction[1]:
                    # Current direction is horizontal
                    if r + 1 < rows and c < len(lines[r + 1]) and lines[r + 1][c] not in {'-', ' ', '+'}:
                        # Going down
                        direction = (1, 0)
                    else:
                        # Going up
                        direction = (-1, 0)
                else:
                    # Current direction is vertical
                    if c + 1 < len(lines[r]) and lines[r][c + 1] not in {'|', ' ', '+'}:
                        # Going right
                        direction = (0, 1)
                    else:
                        # Going left
                        direction = (0, -1)
            elif next_char == ' ':
                break
            curr_pos = (r, c)
            curr = next_char

            # Part 2
            steps += 1

            if curr not in {'-', '|', '+'}:
                letters.append(next_char)

        # Part 1
        answer = ''.join(letters)
        print(answer)
        print(answer, file=f_out)

        # Part 2
        print(steps)
        print(steps, file=f_out)


if __name__ == '__main__':
    main()
