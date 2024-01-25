#https://school.programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    answer = 0
    factor = 0

    reverse_3 = int(str(change3digit(n))[::-1])
    
    # python 진법 바꾸기 쉽게
    # int(x, radix)
    # x : 문자열, radix : 변환하고자 하는 진법
    # answer = int(reverse_3, 3) 
    
    for i in range(len(str(reverse_3))):
        last_digit = reverse_3 % 10
        reverse_3 //= 10
        answer += last_digit * 3**i

    return answer

# 3진법 만들기
def change3digit(n):
    num = ""

    while n > 0:
        num += str(n % 3)
        n //= 3
    
    return num[::-1]


print(solution(125))