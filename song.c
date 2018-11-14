#include <stdio.h>

void sing(void);

int main(void)
{
    sing();
}

void sing(void)
{
    printf("This is the song that doesn't end.\n");
    printf("Yes, it goes on and on my friend.\n");
    printf("Some people started singing it not knowing what it was,\n");
    printf("And they'll continue singing it forever just because...\n");
    sing();
}
