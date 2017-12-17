#!python3

from tqdm import tqdm

def main():
    with open('17_out.txt', 'w') as f_out:
        # Puzzle input
        steps = 303

        # Part 1
        position = 0
        circular_buffer = [0]
        for i in range(1, 2018):
            position = (position + steps) % i
            circular_buffer.insert(position + 1, i)
            position += 1
        answer = circular_buffer[(position + 1) % 2017]
        print(answer)
        print(answer, file=f_out)

        # Part 2
        answer = circular_buffer[1]
        for i in tqdm(range(2018, 50000000 + 1)):
            position = (position + steps) % i
            if position == 0:
                answer = i
            position += 1
        print(answer)
        print(answer, file=f_out)


if __name__ == '__main__':
    main()
