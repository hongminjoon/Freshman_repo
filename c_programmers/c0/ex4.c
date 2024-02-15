#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* s) {
    int total = 0;
    int ten = 1;
    //앞에 부호가 있는 경우
    if(s[0]=='+'|| s[0]=='-')
    {
       for(int i = strlen(s)-1;i>0;i--)
        {
            total = total + ten*(s[i]-'0');
            ten = ten*10;
        }
        if(s[0]=='-')
            total = -1*total;
    }
    //앞에 부호가 없는 경우
    else
    {
        for(int i = strlen(s)-1;i>=0;i--)
        {
            total = total + ten*(s[i]-'0');
            ten = ten*10;
        }
    }
    return total;
}