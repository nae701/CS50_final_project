# Complementary Questions

## Questions

1.1. 10000011

1.2. 11111101

1.3. If the counter is a signed integer and the counter is currently at 01111111, if we
now add 00000010, the counter will overflow into the bit used to denote the sign and now become 10000001.
Since the leftmost digit is now a 1, the computer will process the counter to have a negative value. Essentially if the counter
goes to high such that it overflows into the signed bit, the value could become negative.

1.4. It printed a negative number for the reason described above in answer 1.3 due to the bit being used to determine the sign being overwritten.
After that occured, it kept printing 0, because according to the official C documentation, signed integer overflow results in undefined behaviour.
Printing 0 indefinetely is an example of undefined behavior, since the compiler may have made some assumption that resullted in the value becoming 0.

1.5. Because the system was trying to convert a 64 bit number into a 16 bit number. The developers falsely assumed that the 64 bit number would
not be too large but since it was, it most likely resulted in integer overflow, which then caused other parts of the system using this number to glitch.

## Debrief

a. The cornell notes

b. 45 minutes
