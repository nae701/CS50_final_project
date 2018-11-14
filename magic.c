#include <stdlib.h>
#include <stdio.h>


int main(int argc, char *argv[])
{
    // Ensures file is inputted
    if (argc != 2)
    {
        printf("Usage: magic file\n");
        return 1;
    }

    char *infile = argv[1];

    // Ensures file can be opened
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        printf("Could not open %s\n", infile);
        return 1;
    }

    // Reads first 4 bytes of file into buffer
    unsigned char buffer[4];
    fread(buffer, 1, 4, inptr);

    // Checks if BMP
    if (buffer[0] == 0x42 && buffer[1] == 0x4d)
    {
        printf("BMP\n");
        return 0;
    }

    // Checks if PDF
    if (buffer[0] == 0x25 && buffer[1] == 0x50 && buffer[2] == 0x44 && buffer[3] == 0x46)
    {
        printf("PDF\n");
        return 0;
    }

    // Checks if JPEG
    if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
    {
        printf("JPEG\n");
        return 0;
    }

    fclose(inptr);

    printf("\n");
    return 0;

}

