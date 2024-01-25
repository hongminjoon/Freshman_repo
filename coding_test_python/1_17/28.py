#https://school.programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        line = []
        for j in range(len(arr1[0])):
            line.append(arr1[i][j] + arr2[i][j])
        
        answer.append(line)

    return answer

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]


# map(function, iterable) : iterable = list or tuple
def sumMatrix(A,B):
    return [list(map(sum, zip(*x))) for x in zip(A,B)]

print(sumMatrix(arr1, arr2))

