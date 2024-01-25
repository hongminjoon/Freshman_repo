#https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []
    for i in range(len(arr)):
        if len(answer) == 0:
            answer.append(arr[i])
        
        if arr[i] == answer[-1]:
            continue
        else:
            answer.append(arr[i])

    return answer

print(solution([1,1,3,3,0,1,1]))