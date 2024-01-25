#https://school.programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    answer = ''

    s_list = s.split(' ')

    for s in s_list:
        for i in range(len(s)):
            if i % 2 == 0:
                answer += s[i].upper()
            else:
                answer += s[i].lower()
        answer += ' '

    return answer[:-1]

print(solution("asodnaosnwown ddd"))