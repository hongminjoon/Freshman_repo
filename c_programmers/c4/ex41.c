#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int lottos[], size_t lottos_len, int win_nums[], size_t win_nums_len) {
    int* answer = (int*)malloc(sizeof(int)*3);
    int high =0;
    int low =0;
    
    for(int i=0;i<6;i++)
    {
        if(lottos[i] == 0)
        {high++;}
        else
        {
            for(int j=0;j<6;j++)
            {
                if(lottos[i] == win_nums[j]) //동일한 경우
                {high++; low++;}
            }
        }
    }
    answer[0] = 7-high; 
    answer[1] = 7-low;
    if(high ==0)
        answer[0]=6;
    if (low==0)
        answer[1]=6;
        
    return answer;
}
    