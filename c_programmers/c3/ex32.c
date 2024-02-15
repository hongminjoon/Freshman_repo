#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int a, int b, int n) {
    int answer = 0;
    int new =0;
    
    while(n>=a)
    {
        new = (n / a)*b; 
        answer += new; 
        n %= a; 
        n+= new;
    }
    return answer;
}
