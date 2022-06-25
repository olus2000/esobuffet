import sys

INSTRUCTIONS = list("abcdefgh01!%.+&|^-<>$=@")

Program = list[str | type("Program")]
Stacks = tuple[list[int], list[int], list[int]]

class ExecutionError(RuntimeError):
    pass

def main():
    filename, *data = sys.argv[1:]
    try:
        with open(filename, "r") as file:
            program = compile(file.read())
        run(program, [int(value) for value in data])
    except ExecutionError as e:
        print("Error while executing:", e)
        sys.exit(2)

def compile(program: str) -> Program: 
    stack: list[Program] = [[]]

    for char in program:
        if char in INSTRUCTIONS:
            stack[-1].append(char)
        elif char == "{":
            stack.append([])
        elif char == "}":
            stack[-2].append(stack.pop())
    if len(stack) > 1:
        raise ExecutionError("Not all blocks closed!")
    return stack[0]
    
def run(program: Program, data: list[int]):
    run_block((data, [], []), program, main=True)
    
def run_block(stacks: Stacks, block: Program, main: bool = False):
    a, b, x = stacks
    index: int = 0
    max_index = len(block) - 1
    try:
        while True:
            #print("Executing:", block[index], stacks)
            match block[index]:
                case "a":
                    x.append(a.pop())
                case "b":
                    x.append(b.pop())
                case "c":
                    a.append(x.pop())
                case "d":
                    b.append(x.pop())
                case "e": # Copy content only, no changing references
                    a[:] = b[:]
                case "f": # Copy content only, no changing references
                    b[:] = a[:]
                case "g":
                    a.reverse()
                case "h":
                    b.reverse()
                case "0":
                    x.append(0)
                case "1":
                    x.append(1)
                case "!":
                    x.pop()
                case "%":
                    x += (x.pop(), x.pop())
                case ".":
                    print(x.pop())
                case [*content]:
                    run_block(stacks, content)
                case "+":
                    x.append(x.pop() + x.pop())
                case "&":
                    x.append(x.pop() & x.pop())
                case "|":
                    x.append(x.pop() | x.pop())
                case "^":
                    x.append(x.pop() ^ x.pop())
                case "-": # Bitwise not, not mathematical negation
                    x.append(~x.pop())
                case ">": # Because of the stack, the order is reversed. For these operations order matters
                    second, first = x.pop(), x.pop()
                    x.append(first >> second)
                case "<":
                    second, first = x.pop(), x.pop()
                    x.append(first << second)
                case "$":
                    x.append(x[-1])
                case "=":
                    print("Stacks:", *stacks)
                case "@":
                    raise ExecutionError("Debug exit")

            if index >= max_index:
                if main: 
                    return
                index = 0
            else:
                index += 1
    except IndexError as e:
        if main:
            raise ExecutionError("Index out of bounds in main body!") from e

if __name__ == "__main__":
    main()
