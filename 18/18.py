#!python3

import time
from collections import defaultdict
from multiprocessing import Process, Value, Queue

def main():
    with open('18.txt', 'r') as f, open('18_out.txt', 'w') as f_out:
        instructions = [l.strip().split() for l in f.readlines()]

        # Part 1
        registers = defaultdict(int)
        last_sound = None
        recovered = None
        pc = 0
        # Look I managed to rewrite this using my nice run_process function,
        # but I figured what I commit should be a somewhat faithful representation
        # of the code I actually wrote when solving each part
        while recovered is None:
            if len(instructions[pc]) == 2:
                instruction, reg = instructions[pc]
            if len(instructions[pc]) == 3:
                instruction, reg, arg = instructions[pc]
                try:
                    arg = int(arg)
                except:
                    arg = registers[arg]
            if instruction == 'snd':
                last_sound = registers[reg]
            elif instruction == 'set':
                registers[reg] = arg
            elif instruction == 'add':
                registers[reg] += arg
            elif instruction == 'mul':
                registers[reg] *= arg
            elif instruction == 'mod':
                registers[reg] %= arg
            elif instruction == 'rcv':
                if registers[reg] != 0:
                    recovered = last_sound
            elif instruction == 'jgz':
                if registers[reg] > 0:
                    pc += arg
                    continue
            pc += 1
        print(recovered)
        print(recovered, file=f_out)

        # Part 2
        p1_out = Queue()
        p0_out = Queue()
        p1_send_count = Value('i', 0)
        p1 = Process(target=run_process, args=[instructions, 1, p1_out, p0_out, p1_send_count])
        p0 = Process(target=run_process, args=[instructions, 0, p0_out, p1_out])
        p1.start()
        p0.start()
        # I have no shame. You know you'd do the same thing.
        time.sleep(1)
        p1.terminate()
        p0.terminate()
        print(p1_send_count.value)
        print(p1_send_count.value, file=f_out)


def run_process(instructions, pid, out_q, in_q, send_count=None):
    registers = defaultdict(int)
    registers['p'] = pid
    pc = 0
    while True:
        if len(instructions[pc]) == 2:
            instruction, reg = instructions[pc]
        if len(instructions[pc]) == 3:
            instruction, reg, arg = instructions[pc]
            try:
                arg = int(arg)
            except:
                arg = registers[arg]
        if instruction == 'snd':
            if send_count:
                send_count.value += 1
            out_q.put(registers[reg])
        elif instruction == 'set':
            registers[reg] = arg
        elif instruction == 'add':
            registers[reg] += arg
        elif instruction == 'mul':
            registers[reg] *= arg
        elif instruction == 'mod':
            registers[reg] %= arg
        elif instruction == 'rcv':
            registers[reg] = in_q.get()
        elif instruction == 'jgz':
            try:
                reg = int(reg)
            except:
                reg = registers[reg]
            if reg > 0:
                pc += arg
                continue
        pc += 1


if __name__ == '__main__':
    main()
