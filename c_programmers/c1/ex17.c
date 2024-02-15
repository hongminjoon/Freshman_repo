#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char* solution(int n) {
    char* answer = (char*)calloc(n*3,sizeof(char));
    if(n<=10000)
    {
    if(n%2==0) //짝수인 경우
    {
        //n/2 인 만큼 수박을 더해주면 됨
        for(int i=0;i<n/2;i++)
        {strcat(answer,"수박");}
    }
    else if(n%2!=0) //홀수인 경우
    {
        for(int i=0;i<n/2;i++)
        {strcat(answer,"수박");}
        strcat(answer,"수");
    }
    }
    return answer;
    free(answer);
}

