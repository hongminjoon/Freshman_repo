#https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]

    count = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i%len(answers)] == one[i%len(one)]:
            count[0] += 1
        
        if answers[i%len(answers)] == two[i%len(two)]:
            count[1] += 1

        if answers[i%len(answers)] == three[i%len(three)]:
            count[2] += 1

    return [index + 1 for index, num in enumerate(count) if num == max(count)]

print(solution([1,3,2,4,2]))
