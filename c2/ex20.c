#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
//돈이 충분하면 0 반환
//불충분 -> 차감액 반환 
//price에서 count만큼 증가하며 모두 더해주기 

long long solution(int price, int money, int count) {
    long long sum = 0;
    long long answer = -1;
    long long tmp =price;
    if(price<=2500 && money<=1000000000 && count<=2500)
    {for(int i=0;i<count;i++)
    {
        sum += tmp;
        tmp +=price;
    }
    if(money < sum)
        answer = (-1)*(money - sum);
    else
        answer = 0;}
    printf("%d\n",answer);
    return answer;
}