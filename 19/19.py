#!python3


def main():
    with open('19.txt', 'r') as f, open('19_out.txt', 'w') as f_out:
        lines = f.readlines()

        # Part 1
        answer = 0
        print(answer)
        print(answer, file=f_out)

        # Part 2
        print(answer)
        print(answer, file=f_out)


if __name__ == '__main__':
    main()
