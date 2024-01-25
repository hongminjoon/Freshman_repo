# https://school.programmers.co.kr/learn/courses/30/lessons/1845

# 시간 초과 
# from itertools import combinations
# def solution(nums):
#     answer = 0
    
#     poketmon_list = list(combinations(nums,int(len(nums)/2)))

#     for poketmon in poketmon_list:
#         if len(set(poketmon)) > answer:
#             answer = len(set(poketmon))

#     return answer

def solution(nums):   
    answer = []
    for num in nums:
        if len(answer) < len(nums)/2 and num not in answer:
            answer.append(num)
            
    return len(answer)

print(solution([3,1,2,3]))