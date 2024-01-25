#https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):

    alpha = {"zero":"0", "one":"1", "two":"2", "three":"3", 
            "four":"4", "five":"5", "six":"6", "seven":"7",
            "eight":"8", "nine":"9"}
    
    answer = ""
    numStr = ""
    for char in s:
        if numStr in alpha:
                answer += alpha[numStr]
                numStr = ""
        
        if char.isdigit():
            answer += char
        else:
            numStr += char 
    
    if numStr in alpha:
        answer += alpha[numStr]
    
    return int(answer)

print(solution("123"))