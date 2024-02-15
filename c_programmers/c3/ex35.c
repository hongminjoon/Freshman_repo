#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(int a, int b) {
    // 리턴할 값은 메모리를 동적 할당해주세요.
    //char* answer = (char*)malloc(...);
    int month[12] = {31,29,31,30,31,30,31,31,30,31,30,31};
    char* day[7] = {"FRI","SAT","SUN","MON","TUE","WED","THU"};
    int cnt =0;
    for(int i=0;i<a-1;i++)
    {
        cnt+=month[i];
    }
    cnt+=b;
    if(cnt%7 == 1)
        return day[0];
    else if(cnt%7==2)
        return day[1];
    else if(cnt%7==3)
        return day[2];
    else if(cnt%7 ==4)
        return day[3];
    else if(cnt%7==5)
        return day[4];
    else if(cnt%7==6)
        return day[5];
    else if(cnt%7 ==0)
        return day[6];
    
}

