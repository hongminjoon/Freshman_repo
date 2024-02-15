#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#define swap(a,b) {int tmp = a; a = b; b=tmp;}

// score_len은 배열 score의 길이입니다.
int* solution(int k, int score[], size_t score_len) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(sizeof(int)*score_len+1);
    int* place = (int*)malloc(sizeof(int)*(k+2));
    memset(place,-1,sizeof(int)*(k+2));
    /*
    1. for문에서 k만큼 올림차순 (새로운 스코어 자리 해주는 것)
    2. [0]번째 스코어 값 answer에 담기 
    */
    
    for(int i=0;i<score_len;i++) //일차 만큼
    {
        place[k] = score[i];
        for(int j=0;j<k;j++) //명예의 전당에서 새로운 score받아서 올림차순 & 최하 점수 answer에 기입
        {
            for(int q=j+1;q<=k;q++)
            {
                if(place[j] < place[q])
                    swap(place[j],place[q]);
            }
        }
        int min =10000;
        for(int z=0;z<k;z++)
        {
            if(place[z]>=0&&min > place[z])
                min = place[z];
        }
        answer[i] = min;
    }
    
    return answer;
}
int main()
{
    int score[10]={0, 300, 40, 300, 20, 70, 150, 50, 500, 1000};
    int k = 4;
    solution(k,score,10);
}
