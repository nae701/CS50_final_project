from cs50 import get_string
import sys
from sys import argv

# Ensures proper input from user
if len(argv) != 2:
    sys.exit('Usage: python caesar.py key')
key = int(argv[1])
ptext = get_string('plaintext: ')
print('ciphertext: ', end='')

# Encrypts each letter while preserving case
for c in ptext:
    if c.islower():
        print(c.replace(c, chr((ord(c) - ord('a') + key) % 26 + ord('a'))), end='')
    elif c.isupper():
        print(c.replace(c, chr((ord(c) - ord('A') + key) % 26 + ord('A'))), end='')
    else:
        print(c, end='')
print('')