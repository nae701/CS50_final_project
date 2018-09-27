
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Declares prototype of function
int shift(char c);
int key;

int main(int argc, string argv[])
{
    // Validating key
    // Ensures only one argument is input
    if (argc == 2)
    {
        // Iterates over each char in key to check for all alphabetic characters
        for (int i = 0; i < strlen(argv[1]); i++)
        {
            // If not alphabetic, returns error message
            if (!isalpha(argv[1][i]))
            {
                printf("Usage: %s keyword\n", argv[0]);
                return 1;
            }
        }
        // Sets keyword equal to user input
        string keyword = argv[1];
        // Prompts for plaintext
        string ptext = get_string("plaintext: ");
        printf("ciphertext:");
        // Iterates over plaintext
        for (int i = 0, j = 0; i < strlen(ptext); i++)
        {
            // Shifts each char by the corresponding char in the keyword while preserving uppercase
            if (isupper(ptext[i]))
            {
                // Accounting for case where keyword is too short and must repeat
                ptext[i] = (ptext[i] - 'A' + shift(keyword[j % strlen(keyword)])) % 26 + 'A';
                printf("%c", ptext[i]);
                j++;
            }
            // Shifts each char by the key while preserving lowercase
            else if (islower(ptext[i]))
            {
                // Accounting for case where keyword is too short and must repeat
                ptext[i] = (ptext[i] - 'a' + shift(keyword[j % strlen(keyword)])) % 26 + 'a';
                printf("%c", ptext[i]);
                j++;
            }
            // Does not shift other chars such as punctation, and does not increase counter j
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
        printf("Usage: %s keyword\n", argv[0]);
        return 1;
    }
}
// Determines numeric value of inputted char regardless of case
int shift(char c)
{
    int value;
    // Subtracts appropriate number based on case
    if (isupper(c))
    {
        value = c - 'A';
        return value;
    }
    else
    {
        value = c - 'a';
        return value;
    }
}





