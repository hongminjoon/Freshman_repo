#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
/*
-for문으로 n만큼돌리기
-if(i*i==n)인 경우 tmp = i+1 -> break
-만일 제곱 수가 없는 경우 tmp=0이라면 -1 반환
*/
long long solution(long long n) {
    long long answer = -1;
    for(long long i=1;i<=(n);i++)
    {
        if((i*i)==n)
        {
            answer = (i+1)*(i+1);
            break;
        }
        if(i*i>n)
            break;
    }

    return answer;
}