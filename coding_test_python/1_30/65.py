#https://school.programmers.co.kr/learn/courses/30/lessons/140108

def solution(s):
    answer = 0

    is_x = True
    same_cnt = 0
    diff_cnt = 0
    for char in s:
        if is_x:
            x = char
            is_x = False
            answer += 1
        
        if char == x:
            same_cnt += 1
        elif char != x:
            diff_cnt += 1

        if same_cnt == diff_cnt:
            is_x = True
            same_cnt = 0
            diff_cnt = 0 

    return answer

print(solution("abracadabra"))