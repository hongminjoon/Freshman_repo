
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// number_len은 배열 number의 길이입니다.
int solution(int number[], size_t len) {
    int answer = 0;
    int one =0,two=0,three=0;
    for(int i=0;i<=len-3;i++)
    {
        for(int j=i+1;j<=len-2;j++)
        {
            for(int k=j+1;k<=len-1;k++)
            {
                if(number[i]+number[j]+number[k] == 0)
                    answer++;
            }
        }
    }
    return answer;
}