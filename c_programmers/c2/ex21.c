#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
//48 - 0 , 57 - 9
bool solution(const char* s) {
    bool answer = false;
    int cnt =0;

    if(strlen(s)==4||strlen(s)==6) //문자열 길이 4 혹은 6
    {
        for(int i=0;i<strlen(s);i++)
        {
            if(s[i]>=48 && s[i]<=57) //48 = '0'     57=='9'
            {
                cnt++; 
                printf("%d",cnt);
            }
        }
    }
    if(cnt==strlen(s))
        answer = true;
    return answer;
}