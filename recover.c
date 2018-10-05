#include <stdio.h>
#include <stdlib.h>
//#include <stdbool.h>

#define SIZEJPG 512

int main(int argc, char *argv[])
{
    unsigned char buffer[SIZEJPG] = {0};
    int counterJPG = 0;
    char nameJPG[8] = {0};
    FILE *img = NULL;
    //bool flag = false;


    // ensure proper usage
    if (argc != 2)
    {
        fprintf(stderr, "Usage: recover file\n");
        return 1;
    }

    // remember filename
    char *raw_file = argv[1];

    // open raw file
    FILE *inptr = fopen(raw_file, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", raw_file);
        return 2;
    }

    // Iterates over each 512 Byte block
    while (fread(buffer, SIZEJPG, 1, inptr) == 1)
    {
        // Checks if valid JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // If file is already open, closes it
            if (img != NULL)
            {
                fclose(img);
            }

            // if no file is open, changes flag to true since we will open a file now


            // Make a new JPG
            sprintf(nameJPG, "%03i.jpg", counterJPG);
            img = fopen(nameJPG, "w");
            counterJPG++;
        }

        // Writes to image if file is open
        if (img != NULL)
        {
            fwrite(&buffer, SIZEJPG, 1, img);
        }
    }

    // close all files
    fclose(inptr);
    fclose(img);

    // Program ran successfully
    return 0;

}
