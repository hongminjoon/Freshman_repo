#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

/*
삼항연산자 
num = tmp ==10 ? 100 : 200;
(tmp==10인 경우 num에 100을 대입하고 아닌 경우 200 대입)
*/

char* solution(const char* s) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char* answer = (char*)malloc(sizeof(char)*((strlen(s)+1)));
    strcpy(answer,s);
    printf("%d",strlen(answer));
    //answer[strlen(s)] = NULL;
    
    int i=0;
    int tmp =0;
    while(i<strlen(answer))
    {
        int idx = 0; //각 단어 인덱스 위치
        while(s[i]!=' ' && i<strlen(answer) )
        {
            if(idx%2==0) //짝수인 경우 -> 대문자
            {
                answer[i] = answer[i]>='a'&&answer[i]<='z' ? s[i]-32 : s[i] ;

            }
            else
                answer[i] = answer[i]>='A'&&answer[i]<='Z' ? s[i]+32 : s[i] ;

            i++;
            idx++;
        }
        i++;
    }
    return answer;
}
//answer[i] = answer[i]>='a'&&answer[i]<='z' ? -32 : continue 
