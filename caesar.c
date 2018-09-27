#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int key;

int main(int argc, string argv[])
{
    // Validating key
    // Ensures only one argument is input
    if (argc == 2)
    {
        // Iterates over each char in key to check for all digits
        for (int i = 0; i < strlen(argv[1]); i++)
        {
            if (isdigit(argv[1][i]) == 0)
            {
                printf("Usage: %s key\n", argv[0]);
                return 1;
            }
        }
        // Converts key from a string to an int
        key = atoi(argv[1]);
        // Prompts for plaintext
        string ptext = get_string("plaintext: ");
        printf("ciphertext:");
        // Iterates over plaintext
        for (int i = 0; i < strlen(ptext); i++)
        {
            // Shifts each char by the key while preserving uppercase
            if (isupper(ptext[i]))
            {
                ptext[i] = (ptext[i] - 65 + key) % 26 + 65;
                printf("%c", ptext[i]);
            }
            // Shifts each char by the key while preserving lowercase
            else if (islower(ptext[i]))
            {
                ptext[i] = (ptext[i] - 97 + key) % 26 + 97;
                printf("%c", ptext[i]);
            }
            // Does not shift other chars such as punctation
            else
            {
                printf("%c", ptext[i]);
            }
        }
        printf("\n");
    }
    // Prints error message if invalid key is entered
    else
    {
        printf("Usage: %s key\n", argv[0]);
        return 1;
    }
}
