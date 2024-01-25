# https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []

    for command in commands:
        slice_from, slice_to, index = command

        answer.append(sorted(array[slice_from-1:slice_to])[index-1])
    return answer

#print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
