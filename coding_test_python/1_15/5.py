#https://school.programmers.co.kr/learn/courses/30/lessons/12928

def solution(n):
    answer = 0
    
    list = []
    
    for i in range(1,n+1):
        if n % i == 0:
            list.append(i)
    
    answer = sum(list)   
    
    return answer