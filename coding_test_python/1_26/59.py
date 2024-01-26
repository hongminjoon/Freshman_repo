#https://school.programmers.co.kr/learn/courses/30/lessons/161989

def solution(n, m, section):
    answer = 1
    temp = section[0]
    for sec in section:
        if sec > temp+m-1:
            temp = sec
            answer += 1

    return answer

#print(solution(4, 1, [1,2,3,4]))
print(solution(16, 3, [2,3,14,15]))