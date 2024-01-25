#https://school.programmers.co.kr/learn/courses/30/lessons/138477

def solution(k, scores):
    answer = []

    temp = []
    for score in scores:
        temp.append(score)
        temp.sort(reverse=True)
        
        if len(temp) > k:    
            del temp[-1]
        
        answer.append(temp[-1])    
        
    return answer

print(solution(3,[10, 100, 20, 150, 1, 100, 200]))