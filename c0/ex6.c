
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// arr_len은 배열 arr의 길이입니다.
double solution(int arr[], size_t arr_len) {
    double total = 0;

    for( int i=0;i<arr_len;i++)
    {
        if(arr_len >=1 && arr_len <=100 && arr[i]>=-10000 && arr[i] <=10000)
        {total  += arr[i];}
    }
    double answer =  total / arr_len;
    return answer;
}