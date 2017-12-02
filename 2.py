#!python3


def main():
    with open('2.txt', 'r') as f, open('2_out.txt', 'w') as f_out:
        checksum = 0
        for line in f:
            numbers = [int(n) for n in line.split()]
            checksum += max(numbers) - min(numbers)
        print(checksum)
        f_out.write(str(checksum))


if __name__ == '__main__':
    main()
