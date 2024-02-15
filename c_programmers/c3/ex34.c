#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char* solution(const char* cards1[], size_t cards1_len, const char* cards2[], size_t cards2_len, const char* goal[], size_t goal_len) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int cnt1 =0;
    int cnt2 =0;
    
    for(int i=0;i<goal_len;i++)
    {
        if(cnt1 < cards1_len && strncmp(cards1[cnt1],goal[i],strlen(goal[i]))==0)
        {cnt1++;}
        
        else if(cnt2 < cards2_len && strncmp(cards2[cnt2],goal[i],strlen(goal[i]))==0)
        {cnt2++;}
        
        else
        {return "No";} 
    }
    return "Yes"; 
}



