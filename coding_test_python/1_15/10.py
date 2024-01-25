#https://school.programmers.co.kr/learn/courses/30/lessons/12934

def solution(n):
    answer = 0
    
    num = n ** 0.5

    if num == int(num):
        return (int(num)+1)**2
    else:
        return -1

print(solution(144))