
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int answer = 0; 
    if(n>=3 && n<=1000000)
    {for(int i = 1;i<n;i++)
    {
        int tmp = n % i;
        if(tmp == 1)
        {
            answer = i;
            return answer;
        }
    }
    }
    return answer;
}