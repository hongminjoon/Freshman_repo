#https://school.programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    answer = 0

    for i in range(len(absolutes)):
        
        if signs[i] == True:
            answer += absolutes[i]
        if signs[i] == False:
            answer -= absolutes[i]
        
    return answer

print(solution([4,7,12],[True,False,True]))