#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* s) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char* answer = (char*)malloc(sizeof(char)*2);
    int len = strlen(s);
    if(len%2==0)
    {
        answer[0] = s[(len/2)-1] ;
        answer[1] = s[(len/2)] ;
        answer[2] = NULL ;
    }
     else
      {
        answer[0] = s[(len/2)] ;
        answer[1] = NULL ;
    }
        
    return answer;
    free(answer);
}
