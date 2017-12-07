#!python3


def main():
    with open('6.txt', 'r') as f, open('6_out.txt', 'w') as f_out:
        og_banks = [int(n) for n in f.readline().split()]

        # Part 1
        banks = og_banks.copy()
        num_banks = len(banks)
        seen = {tuple(banks)}

        steps = 0
        while True:
            steps += 1
            m, i = list_max(banks)
            banks[i] = 0

            for j in range(i + 1, i + m + 1):
                banks[j % num_banks] += 1

            t = tuple(banks)
            if t not in seen:
                seen.add(t)
            else:
                break

        print(steps)
        print(steps, file=f_out)

        # Part 2
        banks = og_banks.copy()
        num_banks = len(banks)
        seen = {tuple(banks): 0}

        steps = 0
        while True:
            steps += 1
            m, i = list_max(banks)
            banks[i] = 0

            for j in range(i + 1, i + m + 1):
                banks[j % num_banks] += 1

            t = tuple(banks)
            if t not in seen:
                seen[t] = steps
            else:
                loop_len = steps - seen[t]
                print(loop_len)
                print(loop_len, file=f_out)
                break


def list_max(in_list):
    m = max(in_list)
    return (m, in_list.index(m))


if __name__ == '__main__':
    main()
