#https://school.programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    answer = True

    sum = 0
    x_ori = x

    while x > 0:
        temp = x%10
        sum += temp
        x//=10

    if x_ori%sum != 0:
        answer = False

    return answer

print(solution(12))