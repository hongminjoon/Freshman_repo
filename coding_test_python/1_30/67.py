#https://school.programmers.co.kr/learn/courses/30/lessons/160586

def solution(keymap, targets):
    answer = []

    for target in targets:
        count = 0
        for char in target:
            temp = []
            for key in keymap:
                if char in key:
                    temp.append(key.index(char)+1)
                else:
                    temp.append(-1)
            
            filtered_array = [x for x in temp if x != -1]
            if len(filtered_array) == 0:
                count = -1
                break
            else:
                count += min(filtered_array)
        answer.append(count)

    return answer

#solution(["ABACD", "BCEFD"], ["ABCD","AABB"])
solution(["AA"], ["B"])
#solution(["AGZ", "BSSS"], ["ASA","BGZ"])
