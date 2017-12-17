#!python3

from collections import Counter


def main():
    with open('11.txt', 'r') as f, open('11_out.txt', 'w') as f_out:
        line = f.readline().strip()
        steps = line.split(',')
        directions = ['n', 'ne', 'se', 's', 'sw', 'nw']

        # Part 1
        step_counts = Counter(steps)
        pairs = [('n', 's'), ('nw', 'se'), ('ne', 'sw')]
        for a, b in pairs:
            if step_counts[a] > step_counts[b]:
                low, high = b, a
            else:
                low, high = a, b
            step_counts[high] -= step_counts[low]
            step_counts[low] = 0

        no_more = False
        while not no_more:
            no_more = True
            for i, direction in enumerate(directions):
                left = directions[i - 1]
                right = directions[(i + 1) % 6]
                if step_counts[left] > step_counts[right]:
                    low, high = right, left
                else:
                    low, high = left, right
                if step_counts[low] == 0:
                    continue
                no_more = False
                step_counts[high] -= step_counts[low]
                step_counts[direction] += step_counts[low]
                step_counts[low] = 0
        total_steps = sum(step_counts.values())
        print(total_steps)
        print(total_steps, file=f_out)

        # Part 2
        max_steps = 0
        step_counts = {d: 0 for d in directions}
        opposite = {d: directions[(i + 3) % 6] for i, d in enumerate(directions)}
        for step in steps:
            if step_counts[opposite[step]] > 0:
                step_counts[opposite[step]] -= 1
            else:
                step_counts[step] += 1
                for i, direction in enumerate(directions):
                    left = directions[i - 1]
                    right = directions[(i + 1) % 6]
                    if step_counts[left] > step_counts[right]:
                        low, high = right, left
                    else:
                        low, high = left, right
                    if step_counts[low] == 0:
                        continue
                    step_counts[high] -= step_counts[low]
                    step_counts[direction] += step_counts[low]
                    step_counts[low] = 0
                max_steps = max(max_steps, sum(step_counts.values()))

        print(max_steps)
        print(max_steps, file=f_out)


if __name__ == '__main__':
    main()
