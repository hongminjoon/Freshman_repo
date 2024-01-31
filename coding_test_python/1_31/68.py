#https://school.programmers.co.kr/learn/courses/30/lessons/42576

# 시간초과
# import copy
# def solution(participant, completion):
#     answer_list = copy.deepcopy(participant)

#     for part in participant:
#         if part in completion:
#             answer_list.remove(part)
#             completion.remove(part)

#     return answer_list[0]

def solution(participant, completion):
    my_dic = {}
    
    for part in participant:
        my_dic[part] = my_dic.get(part, 0) + 1
    
    print(my_dic)
    
    for com in completion:
        my_dic[com] -= 1
    
    return max(my_dic, key=my_dic.get)


print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
