#!python3


def main():
    with open('9.txt', 'r') as f, open('9_out.txt', 'w') as f_out:
        stream = f.readline().strip()

        total_score = 0
        garbage = 0
        stack = []
        for c in stream:
            if len(stack) == 0:
                stack.append(c)
            elif stack[-1] == '!':
                stack.pop()
            elif c == '!':
                stack.append(c)
            elif stack[-1] == '<':
                if c == '>':
                    stack.pop()
                else:
                    garbage += 1
            elif stack[-1] == '{' and c == '}':
                total_score += len(stack)
                stack.pop()
            elif c == ',':
                    pass
            else:
                stack.append(c)

        # Part 1
        print(total_score)
        print(total_score, file=f_out)

        # Part 2
        print(garbage)
        print(garbage, file=f_out)


if __name__ == '__main__':
    main()
