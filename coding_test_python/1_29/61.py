#https://school.programmers.co.kr/learn/courses/30/lessons/133499

def solution(babbling):
    answer = 0
    can = ["aya", "ye", "woo", "ma"]

    for bab in babbling:
        for c in can:
            if c * 2 not in bab: 
                bab = bab.replace(c, ' ')
            
            if bab.isspace():
                answer+=1
                break
            
    return answer

print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
