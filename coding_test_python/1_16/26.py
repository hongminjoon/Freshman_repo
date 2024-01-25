#https://school.programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    answer = 0

    sum = 0

    for i in range(1, count+1):
        sum += price * i

    if sum < money:
        answer = 0
    else:
        answer = sum - money

    return answer

print(solution(3, 50, 2))