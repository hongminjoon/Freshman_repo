#https://school.programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    answer = 0
    temp = []
    
    while n > 0:
        temp.append(n % 10)
        n//=10

    temp.sort(reverse=True)
    
    for i in range(len(temp)):
        pop = temp.pop(0)
        answer += pop * (10**len(temp))

    return answer
