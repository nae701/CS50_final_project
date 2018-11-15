# Like Magic

## Questions

4.1. BM

4.2. %PDF

4.3. The prescence of magic numbers alone does not guarntee what file type a file is
because there is a small chance it could be a coincidence. For instance, plain text files do not
have magic numbers, but if the plaintext contains bytes at the start that are magic numbers for
a different file format, we arrive at a contradiction.

4.4. The bitwise AND operator only returns 1 if both input bits are also 1.
            f0 is 1111 0000 in binary
Any true input is 1110 xywz in binary, which satisfies zamyla's condition, where x,y,z,w are 0 or 1
            e0 is 1110 0000 in binary


(buffer[3] & 0xf0) == 0xe0, in this condition, when we use the & operator, it will always return 0 for
each of the 4 rightmost bits, and 1 for the 3 leftmost bits. However, the 4th leftmost bit depends on
our inputted hexadecimal. If the inputted hexadecimal also has a 1 in the 4th leftmost bit, the condition will be false
thus our condition is only true if the 4 left most bits correspond to e in hex. The 4 rightmost bits do not matter, as
desired, since any hex digit will be valid, and thus this condition checks whether the 4th byte is any of these sixteen values
with the hex digit ranging from 0-f.


4.5. Because you only have to compare each bit once using &. If you use ||, you are comparing the same value of all 8 bits
of the input to a bunch of bytes ranging from 0xe0 to 0xef, but only 1 bit is changing in between each of these different comparisons,
not all 8 of the bits. This is unneccesary and slow. Using the &, we can reduce the number of comparisons needed, since it doesnt
matter what the 4 rightmost bits are, we only care about the 4 leftmost bits.

4.6. See `magic.c`.

## Debrief

a. Bitwise operators wikipedia

b. 90 minutes
