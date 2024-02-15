#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

//의문점 : 15번 째 줄에서 등호가 < 이게 아닌지..

char* solution(const char* s) {
    char* answer = (char*)malloc(sizeof(char)*(strlen(s)+1));
    strcpy(answer,s);
    for(int i=0;i<strlen(s);i++)
    {
        for(int j=i+1;j<strlen(s);j++)
        {
        if(answer[i]<answer[j])
            {
            printf("%c %c\n",answer[i],answer[j]);
                char tmp= answer[j];
                answer[j] = answer[i];
                answer[i] = tmp;
            }
        }
    }
    return answer;
}
