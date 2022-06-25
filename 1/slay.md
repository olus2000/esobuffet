# SLAY Specification

## SLAY Programs

Programs consist of a sequence of bytes.

## Execution
To execute, programs are hashed using the SHA3-512 algorithm. The next step depends on the architecture.

On x86_64:
- The resulting 64 byte array is XORed by the following byte array: `[182, 18, 146, 93, 235, 245, 110, 160, 61, 229, 102, 93, 222, 36, 70, 4, 240, 1, 32, 73, 205, 58, 249, 12, 229, 165, 212, 84, 66, 121, 185, 174, 150, 114, 145, 83, 200, 55, 190, 107, 182, 154, 30, 162, 176, 113, 56, 59, 64, 212, 77, 228, 146, 113, 70, 178, 97, 57, 34, 103, 220, 225, 38, 154]`. To XOR 2 arrays, each item `i` in `a` is set to `a[i] ^ b[i]`.
- The result is interpreted as a x86_64 machine code function in the Microsoft x64 calling convention (even on other platforms) with 2 arguments. The first argument is a pointer to the input and the second argument is the length of the input. The signature is as follows: `void(char*, int)`.
- This function is called with the proper arguments.

On ARM64:
- The resulting 64 byte array is XORed by the following byte array: `[10, 236, 147, 82, 232, 79, 111, 244, 28, 237, 39, 188, 219, 100, 204, 193, 117, 254, 101, 72, 32, 56, 188, 158, 10, 219, 88, 66, 232, 109, 248, 210, 132, 182, 149, 226, 219, 54, 66, 72, 192, 90, 39, 52, 202, 174, 253, 237, 163, 160, 159, 30, 32, 229, 214, 27, 208, 173, 178, 102, 115, 113, 178, 225]`. The method of XORing is described above.
- The result is appended to a list C.
- The result of the XOR is XORed again with the following byte array: `[222, 250, 255, 37, 168, 252, 255, 96, 225, 11, 95, 135, 4, 4, 0, 145, 132, 0, 1, 139, 225, 3, 0, 170, 37, 0, 128, 82, 34, 0, 64, 57, 35, 4, 64, 57, 95, 0, 3, 107, 137, 0, 0, 84, 5, 0, 128, 82, 35, 0, 0, 57, 34, 4, 0, 57, 33, 4, 0, 145, 63, 0, 4, 235]`.
- The first twelve bytes of the result are appended to the end of list C.
- The bytes of list C are interpreted as an ARM64 machine code function in the C calling convention with 2 arguments, as above.
- This function is called with the proper arguments.

After this, the (now modified) input is printed to standard output.
