#https://school.programmers.co.kr/learn/courses/30/lessons/133502

def solution(ingredient):
    s = []
    answer = 0
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1,2,3,1]:
            answer += 1
            for _ in range(4):
                s.pop()
        
    return answer

solution([1,1,1,2,3,1,2,3,1,2,3,1])
