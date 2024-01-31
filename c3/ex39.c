#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// section_len은 배열 section의 길이입니다.
int solution(int n, int m, int section[], size_t section_len) {
    int  answer = 0;
    int count = 0; //현재 select 인덱스
    
    while(count < section_len)
    {
        int m_cnt = m;// 1 2 3 4 5  
        int first = section[count];
        while(m_cnt>0) //페인트칠 타임 (m)
        {
            if(section[count+1]-first >=m)//페인트 미포함인 경우
            {
                first = section[++count];
                break;
            }
                m_cnt--;
                count++;
        }
        answer ++;
    }
    return answer;
}
