#https://school.programmers.co.kr/learn/courses/30/lessons/136798

def num_divisor(a):
    count = 0
    for i in range(1, int(a**(1/2)) + 1):
        if a % i == 0:
            count+=1
            if i**2 != a:
                count += 1
    return count


def solution(number, limit, power):
    answer = 0

    for i in range(1,number+1):
        temp = num_divisor(i)
        if temp <= limit:
            answer += temp
        else:
            answer += power

    return answer

print(solution(5, 3, 2))