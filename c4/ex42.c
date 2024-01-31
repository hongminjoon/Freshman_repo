
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* s) {
    long long answer = 0;
    char x = s[0] ;
    long long x_cnt=1;
    long long y_cnt=0;
    long long i=1;

    if(strlen(s)==1)
    {
        return 1;
    }
    while(i<strlen(s))
    {
        if(x != s[i]) //다른 글자인 경우
        {y_cnt ++;}
        else if(x == s[i]) //동일 글자인 경우
        { x_cnt ++;}
        i++;
        if(y_cnt == x_cnt)
        {
            x = s[i];
            y_cnt =0;
            x_cnt =0;
            answer ++;
        }
        if(y_cnt!=x_cnt && (i) == strlen(s))
        { answer++; break;}
    }
    return answer;
}