#https://school.programmers.co.kr/learn/courses/30/lessons/12932?language=python3

def solution(n):
    answer = []
    
    while n > 0:
        answer.append(n % 10)
        n//=10
    
    return answer