#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* t, const char* p) {
    int answer = 0;
    for(int i=0;i<=strlen(t)-strlen(p);i++)
    {
        if(strncmp(t+i,p,strlen(p))<= 0)
            answer++ ;
    }
    return answer;
}
