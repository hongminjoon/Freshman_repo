#https://school.programmers.co.kr/learn/courses/30/lessons/147355

def solution(t, p):
    answer = 0
    
    find_boundary = len(t) - len(p) + 1
    for i in range(find_boundary):
        temp = t[i:i+len(p)]
        
        if int(temp) <= int(p):
            answer += 1

    return answer

print(solution("3141592","271"))