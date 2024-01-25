#https://school.programmers.co.kr/learn/courses/30/lessons/135808

def solution(k, m, score):
    answer = 0

    score.sort()
    while len(score) >= m:
        answer += score[-m:][0] * m
        del score[-m:]

    return answer

print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))