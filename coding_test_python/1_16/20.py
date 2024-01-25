# https://school.programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    arr.remove(min(arr))

    if len(arr) == 0:
        arr.append(-1)

    return arr

print(solution([8,1,4,1,3,8,5,6,2]))