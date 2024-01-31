#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// score_len은 배열 score의 길이입니다.
int solution(int k, int m, int score[], size_t score_len) {
    int answer = 0;
    int arr[11] = { 0 }; // 인덱스 1부터 시작

    for(int i=0;i<score_len;i++)
    {arr[score[i]-1]++;} //각 배열에 알맞게 넣는 좋은 방법 (딱 for문 한번으로 가능)
    
    for(int i=k-1;i>=0;i--)
    {
        answer += (arr[i]/m)*(i+1)*m;
        if(i)  //나머지들은 상품가치가 떨어진다 생각 (arr[i]->arr[i-1]로 옮겨주기)
            arr[i-1] += arr[i]%m;
    }
    
    return answer;
}

