#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(int num) {
    // 리턴할 값은 메모리를 동적 할당해주세요
    //동적할당 센스 (5-(num%2))
    char* answer = (char*)malloc(sizeof(char)*(5-(num%2)));
    if(num % 2==0)
    {
        answer = "Even";
    }    
    else
        answer = "Odd";

    return answer;
}