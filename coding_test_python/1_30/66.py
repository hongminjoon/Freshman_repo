#https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    my_list = [1] * (n+1)
    my_list[0] = 0
    
    for i in reserve:
        my_list[i] = 2
    for i in lost:
        my_list[i] -= 1
    
    for index, cloth in enumerate(my_list):
        if index == 0 or index == len(my_list):
            continue
        
        if cloth == 0:
            if index-1 > 0 and my_list[index-1] == 2:
                my_list[index-1] = 1
                my_list[index] = 1
            elif index+1 < len(my_list) and my_list[index+1] == 2:
                my_list[index+1] = 1
                my_list[index] = 1
    return [1 if x == 2 else x for x in my_list].count(1)

print(solution(5, [2,3,4], [1,2,3]))