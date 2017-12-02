#!python3


def main():
    with open('2.txt', 'r') as f, open('2_out.txt', 'w') as f_out:
        grid = [[int(n) for n in line.split()] for line in f.readlines()]
        # Part 1
        checksum = 0
        for row in grid:
            checksum += max(row) - min(row)
        print(checksum)
        print(checksum, file=f_out)

        # Part 2
        div_sum = 0
        for row in grid:
            div_sum += find_quotient(row)
        print(div_sum)
        print(div_sum, file=f_out)


def find_quotient(row):
    num_set = set(row)
    largest = max(row)
    for n in row[:-1]:
        max_multiple = int(largest / n)
        for m in range(2, max_multiple + 1):
            if n * m in num_set:
                return m


if __name__ == '__main__':
    main()
