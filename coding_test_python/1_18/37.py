#https://school.programmers.co.kr/learn/courses/30/lessons/131705

def solution(number):
    answer = 0

    for i in range(len(number)-2):
        for j in range(i+1, len(number)-1):
            for k in range(j+1, len(number)):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1

    return answer

print(solution([-3, -2, -1, 0, 1, 2, 3]))



# combinations가 무작위로 개수를 조합해주는 모듈인듯..

from itertools import combinations

def solution (number) :    
    cnt = 0
    for i in combinations(number,3) :
        if sum(i) == 0 :
            cnt += 1
    return cnt