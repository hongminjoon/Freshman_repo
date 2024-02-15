#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// nums_len은 배열 nums의 길이입니다.
int solution(int nums[], size_t nums_len) {
    int answer = 0;
    bool prime = true;
    for(int i=0;i<nums_len-2;i++)
    {
        for(int j=i+1;j<nums_len-1;j++)
        {
            for(int k=j+1;k<nums_len;k++)
            {   
                prime = true;
                int tmp = nums[i] + nums[j] + nums[k];
                for(int z = 2;z<tmp;z++)
                {
                    if(tmp%z==0)
                    {
                        prime = false;
                        break;
                    }
                }
                if(prime)
                {
                    answer++;
                }
            }
        }
    }
    
    return answer;
}