#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(long long number, long long limit, long long power) {
    long long answer = 0;
    bool pass = true;

    for (long long i = 1; i <= number; i++) {
        long long cnt = 0;
        pass = true;

        if (i == 1) {
            answer += 1;
        } else {
            for (long long j = 1; j*j<=i; j++) { // 루트를 활용하여 효율적으로 약수 찾기
                if (i % j == 0) {
                    if (i / j == j)
                        cnt += 1;
                    else
                        cnt += 2;
                }
                if (cnt > limit) {
                    answer += power;
                    pass = false;
                    break;
                }
            }
            if (pass)
                answer += cnt;
        }
    }
    return answer;
}

