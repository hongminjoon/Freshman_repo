#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// sizes_rows는 2차원 배열 sizes의 행 길이, sizes_cols는 2차원 배열 sizes의 열 길이입니다.
int solution(int** sizes, size_t sizes_rows, size_t sizes_cols) {
    int answer = 0;
    
    //행렬에서 행에다가 큰값을 위치시키기
    for(int i=0;i<sizes_rows;i++)
    {
        if(sizes[i][0] < sizes[i][1])
        {
            int tmp = sizes[i][0];
            sizes[i][0]= sizes[i][1];
            sizes[i][1] = tmp;
        }
    }
    int rows_max =0;
    int cols_max =0;
    
    for(int i=0;i<sizes_rows;i++)
    {
    rows_max = sizes[rows_max][0]<sizes[i][0] ? i:rows_max;
    cols_max = sizes[cols_max][1]<sizes[i][1] ? i:cols_max;
    
    }
    answer = sizes[rows_max][0]*sizes[cols_max][1];
    return answer;
}