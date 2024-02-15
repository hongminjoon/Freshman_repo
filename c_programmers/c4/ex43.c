#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#define swap(a,b) {char tmp = a ; a = b; b=tmp;}

char* solution(const char* X, const char* Y) {
    char* answer = (char*)malloc(sizeof(char)*3000001);
    int x_cnt[10]={0};
    int y_cnt[10]={0};
    int cnt = 0; 

    for(int i=0;i<strlen(X);i++)
    {x_cnt[X[i]-'0']++;}
    
    for(int i=0;i<strlen(Y);i++)
    {y_cnt[Y[i]-'0']++;}
    
    for(int i=9;i>=0;i--)
    {
        int tmp =0 ;
        char temp = 0;
        if(x_cnt[i] == y_cnt[i])
        {
            while(tmp<x_cnt[i])
            {
                temp = i+'0';
                answer[cnt] = temp;
                cnt++;
                tmp++;
            }
        }
        else
        {
            tmp = x_cnt[i]<y_cnt[i] ? x_cnt[i] : y_cnt[i];
            while(tmp)
            {
                temp = i+'0';
                answer[cnt] = temp;

                cnt++;
                tmp--;
            }
        }
    }
    if(answer[0]==NULL)
        return "-1"; 
    if(answer[0]<1+'0')
        return "0";
    return answer;
}

