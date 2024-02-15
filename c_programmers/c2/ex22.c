
#include <stdio.h>

int main(void) {
    int a;
    int b;
    scanf("%d %d", &a, &b);
    if(a>=1&&a<=1000&&b>=1&&b<=1000)
    {
    for(int i = 0;i<b;i++)
    {
        for(int j=0;j<a;j++)
        {
            printf("*");
        }
        printf("\n");
    }
    }
    return 0;
}