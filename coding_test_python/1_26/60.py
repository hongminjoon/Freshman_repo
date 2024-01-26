#https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = []
    
    length_stage = len(stages)
    for i in range(1, N+1):
        #print(length_stage)
        if length_stage > 0: 
            fail = stages.count(i) / length_stage
            length_stage -= stages.count(i)
            answer.append((i, fail))
        else:
            answer.append((i,0))

        #print("%d번 스테이지 실패율: "%i, fail)

    #print(answer)
    answer.sort(key=lambda x: x[1], reverse=True)
    answer = [x[0] for x in answer]

    return answer

print(solution(4, [1,1,1,1,1]))