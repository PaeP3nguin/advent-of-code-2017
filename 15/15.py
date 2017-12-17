#!python3

from tqdm import tqdm


def main():
    with open('15.txt', 'r') as f, open('15_out.txt', 'w') as f_out:
        # Puzzle inputs
        a_first = 591
        b_first = 393

        a_factor = 16807
        b_factor = 48271
        dividend = 2147483647

        # Part 1
        matches = 0
        gen_a = generator(a_first, a_factor, dividend)
        gen_b = generator(b_first, b_factor, dividend)
        for i in tqdm(range(40 * 1000 * 1000)):
            a_val = next(gen_a)
            b_val = next(gen_b)
            if '{:0>16b}'.format(a_val)[-16:] == '{:0>16b}'.format(b_val)[-16:]:
                matches += 1
        print(matches)
        print(matches, file=f_out)

        a_criteria = 4
        b_criteria = 8

        # Part 2
        matches = 0
        gen_a = generator(a_first, a_factor, dividend, a_criteria)
        gen_b = generator(b_first, b_factor, dividend, b_criteria)
        for i in tqdm(range(5 * 1000 * 1000)):
            a_val = next(gen_a)
            b_val = next(gen_b)
            if '{:0>16b}'.format(a_val)[-16:] == '{:0>16b}'.format(b_val)[-16:]:
                matches += 1
        print(matches)
        print(matches, file=f_out)


def generator(init, factor, dividend, criteria=1):
    last = init
    while True:
        curr = (last * factor) % dividend
        if curr % criteria == 0:
            yield curr
        last = curr


if __name__ == '__main__':
    main()
