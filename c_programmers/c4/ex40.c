#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

int solution(const char* babbling[], size_t babbling_len) {
    int answer = 0;
    char str[4][4] = {"aya","ye","woo","ma"};
    int k,j,same;
    bool t;
    for(int i=0;i<babbling_len;i++)
    {
        t = true;
        k = 0;
        same = -1;
        
        while(t){
            for(j=0;j<4;j++)
            {
                if(strncmp(babbling[i]+k,str[j],strlen(str[j]))==0&& same!=j)
                {
                    k += strlen(str[j]);
                    same =j;
                    break;
                }
            }
            if (babbling[i][k] == '\0') break;
            if (j==4) t = false;
        }
        if (t) answer ++;
    }
    return answer;
}