#https://school.programmers.co.kr/learn/courses/30/lessons/87389
def solution(n):
    answer = 0
    temp = 0
    
    while n > temp:
        temp += 1
        
        if (n % temp) == 1:
            answer = temp
            
            return answer