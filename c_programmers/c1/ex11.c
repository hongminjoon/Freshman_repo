#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

//절대값 길이만큼 true/false 확인 -> false인 경우 sum값에서 빼주기
//answer += signs[i] ? absolutes[i] : -absolutes[i]; -> 간략한 방식
int solution(int absolutes[], size_t absolutes_len, bool signs[], size_t signs_len) {
    int answer = 123456789;
    int sum =0;
    for(int i=0;i<absolutes_len;i++)
    {
        if(signs[i]==false)
        {
            sum = sum - absolutes[i];
        }
        else
            sum = sum + absolutes[i];
    }
    answer = sum;
    return answer;
}
