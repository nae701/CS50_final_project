#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int key;

int main(int argc, string argv[])
{
    //validating key
    //ensures only one argument is input
    if (argc == 2)
    {
        //Iterates over each char in key to check for all digits
        for (int i = 0; i < strlen(argv[1]); i++)
        {
            if (isdigit(argv[1][i]) == 0)
            {
                printf("Usage: %s key\n", argv[0]);
                return 0;
            }
        }
        //converts key from a string to an int
        key = atoi(argv[1]);
        //prompts for plaintext
        string ptext = get_string("plaintext: ");
        printf("ciphertext:");
        //iterates over plaintext
        for (int i = 0; i < strlen(ptext); i++)
        {
            //shifts each char by the key while preserving uppercase
            if (isupper(ptext[i]))
            {
                ptext[i] = (ptext[i] - 65 + key) % 26 + 65;
                printf("%c", ptext[i]);
            }
            //shifts each char by the key while preserving lowercase
            else if (islower(ptext[i]))
            {
                ptext[i] = (ptext[i] - 97 + key) % 26 + 97;
                printf("%c", ptext[i]);
            }
            //does not shift other chars such as punctation
            else
            {
                printf("%c", ptext[i]);
            }
        }
        printf("\n");
    }
    //prints error message if invalid key is entered
    else
    {
        printf("Usage: %s key\n", argv[0]);
        return 0;
    }
}
