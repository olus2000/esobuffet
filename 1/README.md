# Three Stack Bit Math
This esolang has three stacks; A, B and X. The first two, A and B, are used for data storage. A will automatically contain any command line arguments after the program name. X is used for calculations. 

The main logic will be performed using bit magic as comparison operators don't exist. Blocks can be used for limited conditional logic. I haven't confirmed, but it seems to me like this esolang isn't turing complete.

## Blocks
Blocks are the main conditional element in the language. The work by infinetly looping until a stack access is attempted on an empty stack. 

## Instructions
### Block
 * `{`: Opens a block
 * `}`: Closes a block

### Constants
 * `0`: Loads the constant 0 to the X 
 * `1`: Loads the constant 1 to the X 

### Move
 * `a`: Moves one value from A to X
 * `b`: Moves one value from B to X
 * `c`: Moves one value from X to A
 * `d`: Moves one value from X to B
 * `e`: Copies all values from B to A
 * `f`: Copies all values from A to B
 * `g`: Reverses A
 * `h`: Reverses B

### Misc
 * `!`: Pops one value from X
 * `%`: Swaps the top two values of X
 * `.`: Pops and prints the top value of X
 * `$`: Dupelicates the top value of X

### Math and Bit Magic
 * `+`: Adds together the top two values of X
 * `&`: Preforms a bitwise AND operation on the top two values of X
 * `|`: Preforms a bitwise OR operation on the top two values of X
 * `^`: Preforms a bitwise XOR operation on the top two values of X
 * `-`: Preforms a bitwise NOT operation on the top two values of X
 * `<`: Performs a bitshift left on the top two values of X
 * `>`: Performs a bitshift right on the top two values of X

### Debug
 * `@`: Forces the program to exit
 * `=`: Dumps the stacks' contents

## Usage
Run the interpretter using python 3.10 or newer with the program as the first argument and the data as the rest