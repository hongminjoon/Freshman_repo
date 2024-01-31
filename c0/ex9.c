#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool solution(int x) {
    bool answer = true;
    int x_tmp = x;
    int sum =0;
    while(x_tmp)
    {
        sum += x_tmp%10;
        x_tmp /=10;
    }
    if(x%sum !=0)
        answer = false;
    return answer;
}

