#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// numbers_len은 배열 numbers의 길이입니다.
int solution(int numbers[], size_t numbers_len) {
    int answer = 0;
    int cnt =0;
    int i=0,j=0;
    for(i=0;i<=9;i++) //각 배열에서 숫자 0-9 존재 유무를 모두 확인
    {
        cnt =0;
        for(j=0;j<numbers_len;j++) //배열 크기만큼
        {
            if(i == numbers[j]) 
            {
                cnt=1;
                break;
            }
        }
        if(cnt==0)
            answer += i;
    }
    return answer;
}
