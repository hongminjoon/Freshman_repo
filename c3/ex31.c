#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// numbers_len은 배열 numbers의 길이입니다.
int* solution(int numbers[], size_t numbers_len) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    //int* answer = (int*)malloc(sizeof(int)*10);
    int* answer = (int*)malloc(sizeof(int) * 10000);
    memset(answer, 0, sizeof(int) * 10000);
    
    int cnt =0;
    int k =0;   
    bool same = false;
    
    
    for(int i=0;i<numbers_len;i++) 
    {
        for(int j=i+1;j<numbers_len;j++)
        {
                int tmp = numbers[i]+numbers[j];
                same = false; 
                for(int z=0;z<cnt;z++)
                {
                    if(answer[z] == tmp)
                        same = true;
                }
            if(same ==false)
                answer[cnt++] = tmp;
        }
    }
    
    for(int i=0;i<cnt;i++)
    {
        for(int j=i+1;j<cnt;j++)
        {
            if(answer[i]> answer[j])
            {
                int temp = answer[i];
                answer[i] = answer[j];
                answer[j] = temp;
            }
        }
    }
    
    return answer;
}
