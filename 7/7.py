#!python3

from collections import Counter

def main():
    with open('7.txt', 'r') as f, open('7_out.txt', 'w') as f_out:
        lines = f.readlines()

        # Part 1
        programs = set()
        seen = set()
        weights = {}
        children = {}
        for line in lines:
            tokens = line.strip().split()
            program = tokens[0]
            weight = int(tokens[1][1:-1])

            programs.add(program)
            weights[program] = weight

            if len(tokens) > 2:
                child_list = line.strip().split('-> ')[1].split(', ')
                children[program] = child_list
                seen.update(child_list)

        bottom = programs.difference(seen).pop()
        print(bottom)
        print(bottom, file=f_out)

        # Part 2
        # I have a feeling that this code is gonna get me on Santa's naughty list
        try:
            find_balance(bottom, weights, children)
        except Exception as err:
            wrong_weight = err.args[0]
        print(wrong_weight)
        print(wrong_weight, file=f_out)


def find_balance(program, weights, children):
    if program not in children:
        return weights[program]
    else:
        child_weights = [find_balance(p, weights, children) for p in children[program]]
        count = Counter(child_weights)
        if len(count) == 1:
            return sum(child_weights) + weights[program]
        else:
            descending_count = count.most_common()
            right_total_weight = descending_count[0][0]
            wrong_total_weight = descending_count[1][0]
            wrong_child = children[program][child_weights.index(wrong_total_weight)]
            weight_diff = right_total_weight - wrong_total_weight
            right_weight = weights[wrong_child] + weight_diff
            raise Exception(str(right_weight))


if __name__ == '__main__':
    main()
