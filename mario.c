#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height = 0;
    
    //Ensures that user inputs a valid height
    while (height < 1 || height > 8) 
    {
        height = get_int("Enter a height from 1 to 8 inclusive\n");
    }
    
    //Iterated for loop in order to sequentially print the hashes in a pyramid fashion
    for (int i = 0; i < height; i++)
    { 
        //Enters spaces so that pyramid is right-aligned
        for(int k = 0; k < height - i - 1; k++)
        {
            printf(" ");
        }
        
        for(int j = 0; j <= i; j++)
        {
            printf("#");  
        }
        
        printf("\n");
    }
}
