#!python3

import os

TEMPLATE = '''
#!python3


def main():
    with open('{0}.txt', 'r') as f, open('{0}_out.txt', 'w') as f_out:
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

'''

def main():
    cwd = os.getcwd()
    existing_files = set(os.listdir(cwd))
    for i in range(1, 25 + 1):
        dir_name = str(i)
        if dir_name in existing_files:
            continue
        os.mkdir(dir_name)
        with open(f'{i}/{i}.py', 'w+') as code, open(f'{i}/{i}.txt', 'w+') as in_file:
            print(TEMPLATE.format(i), file=code)


if __name__ == '__main__':
    main()
