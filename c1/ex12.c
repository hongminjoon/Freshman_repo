#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(long long num) {
    int answer = -1;
    if(num==1)
        return 0; //주어진 수가 1인 경우
    for(int i=1;i<=500;i++)
    {        
        if(num%2==0) //1-1
            num = num/2;
        else
            num = (num*3)+1; //1-2
        if(num==1 )
        {
            answer=i;
            break;
        }
    }
    return answer;
}


