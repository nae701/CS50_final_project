from cs50 import get_string
from sys import argv
import sys


def main():
    # Ensures valid input is collected from user
    if len(argv) != 2:
        sys.exit('Usage: python bleep.py dictionary')

    dictionary = argv[1]
    bannedWords = []

    # Opens dictionary and adds banned words into a list
    with open(dictionary, 'r') as file:
        for line in file:
            bannedWords.append(line.strip())

    message = get_string('What message would you like to censor?\n')

    # Checks if word is banned, and bleeps it out if banned, else prints normally
    for msgWord in message.split():
        if msgWord.lower() in bannedWords:
            # Iterates each character and prints star instead
            for c in msgWord:
                print('*', end='')
            print(' ', end='')
        else:
            print(msgWord, end=' ')
    print()


if __name__ == "__main__":
    main()