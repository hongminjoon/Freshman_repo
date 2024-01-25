#https://school.programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    gcd = 0 #최대공약수
    lcm = 0 #최소공배수

    #최대공약수
    for i in range(1, max(n,m)+1):
        if n%i == 0 and m%i ==0:
            gcd = i

    #최소공배수 = 두 개의 수 곱하고 최대공약수 나눔
    lcm = int(n * m / gcd)

    answer = [gcd, lcm]
    
    return answer

print(solution(3, 12))