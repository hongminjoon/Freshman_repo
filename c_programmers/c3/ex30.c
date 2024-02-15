#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char* solution(int food[], size_t food_len) {
    char* answer = (char*)malloc(sizeof(char)*100000);

    int cnt = 0; 
    for(int i=1;i<food_len;i++) //앞에서 시작하는 사람먼저 answer에 기입
    {
        int tmp = food[i]/2;
        if(tmp >0)
        {  
            int j=0;
            while(j < tmp)
            {
                answer[cnt++] = i+'0'; 
                j++;
            }
        }
    }
    answer[cnt] = '0'; //중간에 0 넣어주기
    
    int count =cnt ; //뒷 사람 넣는 count 
    for(int i = cnt-1;i>=0;i--) //앞사람 데이터 뒤에서부터 복붙
    {
        answer[++count] = answer[i];
    }
    answer[++count] = '\0'; //마지막에 쓰레기값 처리
    return answer;
}
