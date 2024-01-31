#include <stdbool.h>
#include <stdlib.h>
//left에서right까지 약수의 개수가 짝수인 경우 더해주고, 홀수인 경우 빼준다.
int solution(int left, int right) {
    int answer = 0;
    int cnt =0;
    for(int i=left;i<=right;i++)
        {
            cnt=0; //cnt 초기화
         for(int k=1;k<=i;k++)
         {
             if(i%k==0)
                 cnt++;
         }
        if(cnt%2==0) //약수의 개수가 짝수인 경우 
            answer += i;
        else
            answer -= i;
        }
    return answer;
}
