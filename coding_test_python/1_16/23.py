# https://school.programmers.co.kr/learn/courses/30/lessons/12922

def solution(n): # mine
    answer = ''

    for i in range(n):
        if len(answer) == 0:
            answer += '수'

        elif answer[-1] == '수':
            answer += '박'

        else:
            answer += '수'

    return answer

def water_melon(n): # best I think
    return "수박" * (n//2) + "수" * (n%2)