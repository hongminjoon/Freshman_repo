#https://school.programmers.co.kr/learn/courses/30/lessons/131128

# 시간초과
# def solution(X, Y):
#     answer = ""

#     x_list = sorted([x for x in X], reverse=True)
#     y_list = [y for y in Y]

#     for x in x_list:
#         if x in y_list:
#             answer += x
#             y_list.remove(x)
    
#     if not answer:
#         return "-1"
    
#     return str(int(answer))

# 시간초과
# def solution(X, Y):
#     answer = ""

#     x_list = sorted([x for x in X], reverse=True)
#     y_list = [y for y in Y]

#     for x in x_list:
#         if x in y_list:
#             answer += x
#             y_list.remove(x)
    
#     if not answer:
#         return "-1"
    
#     if(answer[0] == '0'):
#         return '0'
              
#     return answer


# 해결법 
# 참고 : https://school.programmers.co.kr/questions/57297
def solution(X, Y):
    answer = ""
    x_list = [0,0,0,0,0,0,0,0,0,0]
    y_list = [0,0,0,0,0,0,0,0,0,0]

    for x in X:
        index = int(x)
        x_list[index] += 1

    for y in Y:
        index = int(y)
        y_list[index] += 1

    for i in range(9, -1, -1):
        while x_list[i] and y_list[i]:
            answer += str(i)
            x_list[i] -= 1
            y_list[i] -= 1

    if not answer:
        return "-1"
    
    # return str(int(answer)) # 시간초과
    
    if(answer[0] == '0'):
        return '0'
              
    return answer

print(solution("100", "2345"))