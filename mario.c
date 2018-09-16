#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height = 0;
    
    while (height < 1 || height > 8) 
    {
        height = get_int("Enter a height from 1 to 8 inclusive\n");
    }
    
    for (int i = 0; i < height; i++)
    { 
        for(int k = 0; k < height - i - 1; k++)
        {
            printf(" ");
        }
        
        for(int j = 0; j <= i; j++)
        {
            printf("#");  
        }
        
        printf("  ");
        
        for(int l = 0; l <= i; l++)
        {
            printf("#");  
        }
        
        printf("\n");
    }
}

