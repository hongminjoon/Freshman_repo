#https://school.programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    answer_list = []
    index = -1
    num = ''
    for char in dartResult:

        if char.isalpha():
            answer_list.append(int(num) ** {'S': 1, 'D': 2, 'T': 3}[char.upper()])
            index += 1
            num = ''

        elif char.isdecimal():
            num += char
    
        else:
            if char == '*':
                if index > 0:
                    answer_list[index-1] *= 2
                    answer_list[index] *= 2
                else:
                    answer_list[index] *= 2
            else:
                answer_list[index] *= (-1)

    return sum(answer_list)

print(solution("1S2D*3T"))