
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(long long n) {
    /*
    -n은 10,000,000,000이하인 자연수 -> 최대 10^11로 동적할당 크기 = 11
    */
    int* answer = (int*)malloc(sizeof(int)*1);
    int cnt = 0;
    while(n)
    {
        answer[cnt] = n%10;
        n/=10;
        cnt++;
    }
    return answer;
}