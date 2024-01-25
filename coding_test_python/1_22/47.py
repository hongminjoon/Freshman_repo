# https://school.programmers.co.kr/learn/courses/30/lessons/132267

def solution(a, b, n):
    answer = 0
    
    while n >= a:       
        new_n = n // a * b
        remind = n % a
        
        answer += new_n

        n = new_n + remind

    return answer

print(solution(999999, 4, 999999))