#!python3

def main():
    with open('1.txt', 'r') as f, open('1_out.txt', 'w') as f_out:
        captcha = [int(n) for n in f.readline().strip()]
        captcha.append(captcha[0])
        captcha_sum = 0
        for a, b in zip(captcha[:-1], captcha[1:]):
            if a == b:
                captcha_sum += a
        print(captcha_sum)
        f_out.write(str(captcha_sum))

if __name__ == '__main__':
    main()
