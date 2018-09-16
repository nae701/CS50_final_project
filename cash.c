#include <cs50.h>
#include <stdio.h>
#include <math.h>

//Program to determine the mininum number of coins needed to make change
int main (void)
{
    float change ;
    
    //Collect user input on change owed
    do
    {        
        change = get_float("How much change is owed?\n");   
    }
    while (change < 0);
    
    //Converts change into a cent amount
    int cents = round(change*100);
    
    //Finds the number of times each coin goes into cents starting with quarters then         dimes then nickels
    
    int quarters = cents / 25;    
    cents = cents % 25;
    
    int dimes = cents / 10;    
    cents = cents % 10;
    
    int nickels = cents / 5;    
    cents = cents % 5;
    
    int pennies = cents;
    
    //Sums the number of coins then prints sum
    int coins = quarters + dimes + nickels + pennies;
    printf("%i\n", coins);
    
}
