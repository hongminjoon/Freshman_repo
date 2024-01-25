#https://school.programmers.co.kr/learn/courses/30/lessons/12918

def solution(s):
    answer = False
    if len(s) == 4 or len(s) == 6:
        answer = s.isdigit()
    
    return answer

print(solution("123458"))

def solution(s):
    return s.isdigit() and len(s) in [4,6]