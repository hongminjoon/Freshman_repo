#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* s) {
    long long answer = 0;
    long long len = strlen(s);
    char* dig[10] = {"zero","one","two","three","four","five","six","seven","eight","nine"};
    long long ten = 1;
    char tmp[10];
    int j=0;
    
    for(int i=0;i<len;i++)
    {
        if(s[i] >= 48&& s[i]<=57)//숫자인 경우
        {
                answer *=10;
                answer +=(s[i]-'0');
        }
        else //영어인 경우
        {
            tmp[j++] = s[i];
            tmp[j] = '\0';
            
            for(int k=0;k<10;k++) //영어나올 때 마다 dig이랑 비교해보기
            {
                if(strncmp(tmp,dig[k],strlen(dig[k]))==0)
                {
                    answer*=10;
                    answer += k;
                    j=0;
                    break;
                }
            }
        }
    }
    return answer;
}


int main()
{
    char* s =  "48one7";
    printf("%d",solution(s));

}
