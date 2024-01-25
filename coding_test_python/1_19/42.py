#https://school.programmers.co.kr/learn/courses/30/lessons/134240

def solution(food):
    answer_list = [0]
    
    for i in range(len(food)-1,0,-1):

        num_food = food[i] // 2
        for j in range(num_food):
            answer_list.append(i)
            answer_list.insert(0,i)
    

    return "".join(map(str,answer_list))

print(solution([1,3,4,6]))