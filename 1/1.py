#!python3

def main():
    with open('1.txt', 'r') as f, open('1_out.txt', 'w') as f_out:
        captcha = [int(n) for n in f.readline().strip()]
        length = len(captcha)

        # Part 1
        captcha_sum = 0
        for i, n in enumerate(captcha):
            next_index = (i + 1) % length
            if captcha[i] == captcha[next_index]:
                captcha_sum += n
        print(captcha_sum)
        print(captcha_sum, file=f_out)

        # Part 2
        captcha_sum = 0
        halfway = int(length / 2)
        for i, n in enumerate(captcha):
            next_index = (i + halfway) % length
            if captcha[i] == captcha[next_index]:
                captcha_sum += n
        print(captcha_sum)
        print(captcha_sum, file=f_out)

if __name__ == '__main__':
    main()
