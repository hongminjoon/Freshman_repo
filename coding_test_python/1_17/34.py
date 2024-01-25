#https://school.programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    answer = 0

    while d and (budget-min(d)) >= 0:
        budget -= min(d)
        d.remove(min(d))
        answer += 1

    return answer