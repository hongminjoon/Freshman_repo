#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>

int solution(long long n) {
    long long answer = 0;
    long long tmp[100000000] = {0};
    int i=0;
    while(n/3>0) //10->3
    {
        tmp[i] = n%3;
        i++;
        n = n/3;
    }
    tmp[i] = n%3;
    int k=0; //tmp배열의 정수
for(int j=i;j>=0;j--) //3->10
{
    answer += tmp[j]*(pow(3,k));
    k++;
}
    return answer;
}
