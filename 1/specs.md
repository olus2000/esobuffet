# Stack sorter

Stack sorter is a concatenative language based on the concatenative calculus.
It operates via the means of expression rewriting.
Expressions may consist of:
    - operators
    - quotations
    - numbers (only during runtime, not representable in code)


### Operation

The program is parsed into an expression according to the rules explained
below. Input is parsed as a string of whitespace-separated decimal numbers
ending in a newline and prepended to the expression. Any parsing errors may
produce undefined behavior.

The expression is scanned for patterns related to words. The right-most
match is replaced with another expression according to the rule for that
pattern. This match-replace cycle is repeated until there are no matches.

Trailing numbers in the resulting expression are the output of the program.
Only numbers that are outside quotations count for output.


### Operators and patterns

IMPORTANT: patterns don't match within quotations.

There are several words that can be used in the stack sorter, every one
coming with a pattern and a substitution rule. In the examples letters
`X` and `Y` represent arbitrary quotations or numbers, letters `N` and `M`
represents numbers and letter `A` represents an arbitrary expression.
Spaces represent any non-zero number of whitespace delimiters.

    - `NM~`   -> `NM`      if N <= M, else `MN`
    - `XY~`   -> `YX`      if X or Y is not a number, else the rule above matches.
    - `X~`    -> `X`      if previous two rules didn't match.
    - `X[A]+` -> `[XA][AX]`
    - `X[A]!` -> `A`

Any characters except `[]~!+` in the program are discarded.


### Quotations

In code quotations are represented as expressions in brackets: `[]`.
Quotations can be manipulated using operators. Patterns don't match
inside quotations, and numbers contained within them don't count as
trailing numbers.

If brackets in the program don't match it's a parsing error which
produces undefined behavior.


### Examples

Program `[]![]+~!` with input `1 2` will output `1`.

I'm too lazy to write more.


### Interpreter

Interpreter expects one parameter: a file with the program. It will parse the program,
parse one line of input and print out the output if no errors occur.