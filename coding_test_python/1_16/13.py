# https://school.programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    answer = 0

    if a < b:
        for i in range(a, b+1):
            answer += i

    elif a == b:
        answer = a

    else:
        for i in range(a, b-1, -1):
            answer += i

    return answer
