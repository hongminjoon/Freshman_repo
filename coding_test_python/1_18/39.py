#https://school.programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    answer = ''

    for char in s:
        if char.isupper():
            char = chr((ord(char) - ord('A') + n) % 26 + ord('A'))
        elif char.islower():
            char = chr((ord(char) - ord('a') + n) % 26 + ord('a'))
        
        answer += char

    return answer


print(solution("A B",4))