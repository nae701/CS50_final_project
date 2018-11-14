# Complementary Questions

## Questions

7.1. A secure cipher has very few vulnerabilities. For instance, a secure cipher sould be sufficiently random
that even with a large amount of data i.e. plaintext and the corresponding ciphertext, it should be incredibly difficult to find
any pattern. A secure cipher should be of sufficient computational complexity that it is very resistant to brute
force attacks.

7.2. A Caesar cipher is not very secure, since a frequency analysis of the ciphertext could reveal that only a simple
shifting cipher has been used, and from there it is not difficult for an attacker to brute force all possible options for the
shift value. The Caesar cipher does not protect against the potential vulnerabiltiies described in 7.1.

7.3. A slant cipher is not very secure, because if a frequency analysis is done, it would be very similar to plaintext since letters have
not been changed, only their ordering. Depending on the size of the message encrypted, it could be possible for the attack to simply
brute force all possible combinations of the letters. Given ciphertext, it may be possible to determine a pattern by using common letter groupings
such as "QU" since individual letters have not been changed.

7.4. Because each level of depth would only have character, so when you relocate each row back into the original message,
each row has an individual character and would be put back into the original message in the original order, which results in
the message not being ciphered and remaining the same.

7.5. Encrypting a message is a reversible process since it produces ciphertext which can be deciphered if one has the key. But hashing a message
is not a (feasibly) reversible process, even if one has the hash function. Encryption is a one to one function (hence its invertibility) but hashing
can result in collisions since it is possible for multiple inputs to have the same hash.

7.6. See `slanted.py`.

## Debrief

a. lecture 2 notes

b. 70 minutes
