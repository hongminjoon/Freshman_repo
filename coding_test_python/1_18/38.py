#https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    max_list = []
    min_list = []

    for i in range(len(sizes)):
        if sizes[i][0] > sizes[i][1]:
            max_list.append(sizes[i][0])
            min_list.append(sizes[i][1])
        else:
            max_list.append(sizes[i][1])
            min_list.append(sizes[i][0])
  

    max_list.sort(reverse=True)
    min_list.sort(reverse=True)

    answer = max_list[0] * min_list[0]

    return answer


print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))


def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)