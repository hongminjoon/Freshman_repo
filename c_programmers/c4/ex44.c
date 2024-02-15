#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// keymap_len은 배열 keymap의 길이입니다.
// targets_len은 배열 targets의 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int* solution(const char* keymap[], size_t keymap_len, const char* targets[], size_t targets_len) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(sizeof(int)*101);
    bool check = false;
    for(int i=0;i<targets_len;i++) //targets[i]
    {
        for(int j=0;j<strlen(targets[i]);j++) //targets[i][j]
        {
            for(int a = 0;a < keymap_len;a++) //keymap[a]
            {
                if(keymap[a] == targets[i][j])
                {
                    check = true;
                    answer[i]++;
                    break;
                }
            }
            while(!check) //keymap[a][b]
            {
                for(int a = 0;a<keymap_len;a++)
                {
                    for(int b = 0;b<strlen(keymap[a]);b++)
                    {
                        if(keymap[a][b]==targets[i][j])
                        {check = true; answer[i] += (b+1); break; }
                    }
                }
            }
            if(!check)
                return -1;
        }
    }
    return answer;
}
int main()
{
    const char* keymap[] = (char*)malloc(sizeof(char)*6);
    keymap[0] = "ABACD";
    keymap[1] = "BCEFD";
    const char* targets[] = (char*)malloc(sizeof(char)*6);
    keymap[0] = "ABCD";
    keymap[1] = "AABB";
    printf("%d",solution(keymap,2,targets,2));
}