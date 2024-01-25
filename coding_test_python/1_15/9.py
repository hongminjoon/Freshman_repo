# https://school.programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    answer = True
    num_p = 0
    num_y = 0
    
    for str in s.lower():
        if str == 'p':
            num_p += 1
        if str == 'y':
            num_y += 1
    
    if num_p != num_y:
        return False

    return True
print(solution("pPoooyY"))