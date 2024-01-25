#https://school.programmers.co.kr/learn/courses/30/lessons/12954
def solution(x, n):
    answer = []

    count = 0

    while count < n:
        answer.append(x)
        x += answer[0]
        count+=1
    
    return answer