#!python3


def main():
    with open('4.txt', 'r') as f, open('4_out.txt', 'w') as f_out:
        lines = f.readlines()
        # Part 1
        valid = 0
        for line in lines:
            words = line.split()
            word_set = {w for w in words}
            if len(word_set) == len(words):
                valid += 1
        print(valid)
        print(valid, file=f_out)

        # Part 2
        valid = 0
        for line in lines:
            words = line.split()
            word_set = {''.join(sorted(w)) for w in words}
            if len(word_set) == len(words):
                valid += 1
        print(valid)
        print(valid, file=f_out)


if __name__ == '__main__':
    main()
