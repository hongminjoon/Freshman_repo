
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int ten = 10;
    int answer = 0;
    while(n)
    {
        answer += n%ten;
        n = n/10;
    }
    return answer;
}