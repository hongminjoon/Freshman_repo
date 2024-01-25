def solution(left, right):
    answer = 0

    for i in range(left, right+1):
        num_divisor = len(getDivisor(i))

        if num_divisor%2 == 0:
            answer += i
        else:
            answer -= i

    return answer

def getDivisor(n):

    divisorsList = []

    for i in range(1, n + 1):
        if (n % i == 0) :
            divisorsList.append(i)

    return divisorsList


print(solution(24,27))