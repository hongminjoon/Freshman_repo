#https://school.programmers.co.kr/learn/courses/30/lessons/12921

def is_prime_number(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False 
    return True 

def solution(n):
    answer = 0
    
    for i in range(2, n+1):
        if is_prime_number(i):
            answer += 1

    return answer

print(solution(10))