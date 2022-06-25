from sys import argv

'''
list -> quotation
int -> number
str -> operator
'''


# Will break on 999-deep nested quotations, but I think that's reasonable.
def parse_program(p: str, i: int = 0) -> (list, int):
    program = []
    while i < len(p) and p[i] != ']':
        if p[i] in '~!+':
            program.append(p[i])
        elif p[i] == '[':
            start = i
            quote, i = parse_program(p, i + 1)
            if i >= len(p) or p[i] != ']':
                raise Exception(f'Unclosed quotation at {start}')
            program.append(quote)
        i += 1
    return program, i

def parse_input():
    return [int(s) for s in input().split()]


# When popping two items 'a' will be the leftmost value, 'b' the rightmost.
def reduce(p, dat):
    ret = [p]
    ip = [0]
    while ret:
        if ip[-1] >= len(ret[-1]):
            ret.pop()
            ip.pop()
        else:
##            print(ret, ip, dat, sep='\n')
##            print()
            com = ret[-1][ip[-1]]
            ip[-1] += 1
            match com:
                case int() as i:
                    dat.append(i)
                case list() as q:
                    dat.append(q)
                case '~':
                    if len(dat) > 1:
                        match dat.pop(), dat.pop():
                            case int(a), int(b):
                                if a < b:
                                    dat.append(a)
                                    dat.append(b)
                                else:
                                    dat.append(b)
                                    dat.append(a)
                            case a, b:
                                dat.append(a)
                                dat.append(b)
                case '!':
                    if len(dat) < 2 or not isinstance(dat[-1], list):
                        dat = []
                    else:
                        a, b = dat.pop(), dat.pop()
                        ret.append(a)
                        ip.append(0)
                case '+':
                    if len(dat) < 2 or not isinstance(dat[-1], list):
                        dat = []
                    else:
                        a, b = dat.pop(), dat.pop()
                        dat.append([b] + a)
                        dat.append(a + [b])
                case _:
                    raise Exception(f'Unexpected item in the program: {com}')
    ans = []
    for i in reversed(dat):
        if isinstance(i, int):
            ans.append(i)
        else:
            break
##    print(ans)
##    print(dat)
    return list(reversed(ans))


if __name__ == '__main__':
    if len(argv) != 2:
        raise Exception(f'Wrong number of arguments: {len(argv) - 1}')
    with open(argv[1], 'r') as f:
        program, _ = parse_program(f.read())
    out = reduce(program, parse_input())
    for i in out:
        print(i, end=' ')
    print()
                
