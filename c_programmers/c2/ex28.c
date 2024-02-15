#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

int* solution(const char* s) {
    int* answer = (int*)malloc(sizeof(int)*strlen(s)+1);
    answer[0]= -1; //항상 첫번째꺼는 -1이니까 
    int idx = 0;
    for(int i=1;i<strlen(s);i++)
    {
        idx = 0;
        for(int k=0;k<i;k++)
        {
            if(strncmp(s+k,s+i,1)==0)
            {idx = i-k;}
        }
        answer[i] = idx>0 ? idx:-1;
    }
    
    return answer;
}
