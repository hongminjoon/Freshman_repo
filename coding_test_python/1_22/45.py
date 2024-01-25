# https://school.programmers.co.kr/learn/courses/30/lessons/68644

from itertools import combinations

def solution(numbers):

    return sorted(list(set(map(sum,combinations(numbers,2)))))

print(solution([5,0,2,7]))