#!python3


def main():
    with open('13.txt', 'r') as f, open('13_out.txt', 'w') as f_out:
        lines = f.readlines()

        depths = {}
        for line in lines:
            layer, depth = [int(n) for n in line.strip().split(': ')]
            depths[layer] = depth
        # depths = {0:3, 1:2, 4:4, 6:4}
        max_depth = max(depths.keys())

        # Part 1
        severity = 0
        for depth, r in depths.items():
            if (depth % ((r - 1) * 2)) == 0:
                severity += depth * r
        print(severity)
        print(severity, file=f_out)

        # Part 2
        delay = 0
        while True:
            caught = False
            for depth, r in depths.items():
                if ((delay + depth) % ((r - 1) * 2)) == 0:
                    caught = True
                    break
            if not caught:
                break
            else:
                delay += 1
        print(delay)
        print(delay, file=f_out)


if __name__ == '__main__':
    main()
