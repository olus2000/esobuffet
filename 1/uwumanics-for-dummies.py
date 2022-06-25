# name is short for "uwumanic computer"
#
# cheat sheet:
# 8 registers
# they can only store either a list of ??? or an integer (can be repurposed)
# assembly-like syntax with destination commonly being the first argument
#
# note for the jump instruction: instead of labels it accepts a line number,
# and the first line of the file is number 0.
# blank lines and comments also count as lines.

import sys

def uwu(first, second):
    assert(type(first) is list)
    assert(type(second) is list)
    res = []
    while True:
        if first == []:
            res += second
            return res
        if second == []:
            res += first
            return res
        if first[0] <= second[0]:
            res.append(first[0])
            del first[0]
        else:
            res.append(second[0])
            del second[0]

def manic(integer, array):
    assert(type(array) is list)
    assert(type(integer) is int)
    if integer<0:
        array = array[::-1]
        integer *= -1
    if integer > len(array):
        integer = len(array)
    return (array[:integer], array[integer:])

if __name__ == "__main__":
    filename = sys.argv[1]
    program = open(filename, 'r').read()
    lines = program.splitlines()
    instructions = [line.split() for line in lines]

    pc = 0
    registers = {}
    registers_count = 8
    for i in range(registers_count):
        # no uppercase for you.
        registers[chr(ord('a')+i)] = 0
    def get(s):
        try:
            return int(s)
        except:
            return registers[s]

    while True:
        #print(registers)
        ins = instructions[pc]
        if ins == []: # blank line, ignore
            pc += 1
            continue
        op = ins[0]
        # switch statements are only in python 3.10 and I have 3.9 #debianmoment
        if op == 'cmp' or op == 'compare' or op == '>': # works on arrays as well!
            a = registers[ins[1]]
            b = get(ins[2])
            c = get(ins[3])
            if b<c:
                registers[ins[1]] = -1
            elif b>c:
                registers[ins[1]] = 1
            else:
                registers[ins[1]] = 0
        elif op == 'jmp' or op == 'jump' or op == 'j':
            if len(ins) == 2: # unconditional jump
                a = get(ins[1])
                pc = a+0
            elif len(ins) == 4: # conditional jump
                a = get(ins[1])
                b = get(ins[2])
                c = get(ins[3])
                assert(type(a) is int)
                if a == 0:
                    pc = b+0
                else:
                    pc = c+0
            else:
                raise Exception("incorrect number of arguments to jump instruction")
            continue
        elif op == 'add' or op == '+':
            a = registers[ins[1]]
            b = get(ins[2])
            registers[ins[1]] = a+b+0
        elif op == 'neg' or op == 'negate': # no subtraction
            a = registers[ins[1]]
            registers[ins[1]] = 0-a
        elif op == 'mul' or op == '*' or op == 'multiply':
            a = registers[ins[1]]
            b = get(ins[2])
            assert(type(a) is int)
            assert(type(b) is int)
            registers[ins[1]] = a*b
        elif op == 'hlt' or op == 'halt' or op == 'h':
            break
        elif op == '#' or op == '//' or op == '--' or op == ';' : # comment
            pass
        elif op == 'uwu' or op == '🥺':
            a = registers[ins[1]]
            b = registers[ins[2]]
            registers[ins[1]] = uwu(a,b)
        elif op == "manic" or op == "mnc":
            a = registers[ins[1]]
            b = registers[ins[2]]
            registers[ins[1]], registers[ins[2]] = manic(a,b)
        elif op == 'len' or op == 'length' or op == 'l':
            a = registers[ins[1]]
            b = registers[ins[2]]
            registers[ins[1]] = len(b)
        elif op == 'mov' or op == 'move' or op == 'copy' or op == "=": # it does indeed copy
            a = registers[ins[1]]
            b = get(ins[2])
            registers[ins[1]] = b
        elif op == 'in' or op == 'inp' or op == 'read' or op == 'input' or op == 'i':
            a = registers[ins[1]]
            line = input()
            arr = list(map(int,line.split()))
            registers[ins[1]] = arr
        elif op == 'out' or op == 'print' or op == 'output' or op == 'o':
            a = registers[ins[1]]
            assert(type(a) is list)
            for item in a:
                print(f"{item} ", end="")
            print("")
        else:
            raise Exception("invalid instruction")
        pc += 1


