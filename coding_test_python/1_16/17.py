# https://school.programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    answer = []

    for element in arr:
        if element % divisor == 0:
            answer.append(element)
    
    if len(answer) == 0:
        answer.append(-1)
    
    answer.sort()

    return answer