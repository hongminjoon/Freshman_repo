#https://school.programmers.co.kr/learn/courses/30/lessons/12944
def solution(arr):
    answer = 0
    count = 0
    
    for list in arr:
        answer += list
        count+=1
        
    answer = answer / count
    
    return answer

solution([1,2,3,4])