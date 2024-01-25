# https://school.programmers.co.kr/learn/courses/30/lessons/12917

def solution(s):
    arr = []

    for i in s:
        arr.append(i)

    arr.sort(reverse=True)

    return "".join(arr)


def solution(s):
    return ''.join(sorted(s, reverse=True))