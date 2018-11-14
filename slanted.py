import sys
from cs50 import get_string


def main():

    # Ensure proper usage
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        exit("Usage: python slant.py depth")
    depth = int(sys.argv[1])

    # Encrypt message
    message = get_string("Message: ")
    if len(message) >= depth:
        print("Slanted:", slant(message, depth))


def slant(message, depth):
    # Create new string to store our encrypted message
    cipher = ""

    # Iterates over each level of depth
    for i in range(depth):

        # Starting at that level of depth, iterates over whole message in steps equal to depth
        for j in range(i, len(message), depth):

            # Stores encrypted message by adding each new encrypted letter
            cipher = cipher + message[j]

    return cipher


if __name__ == "__main__":
    main()
