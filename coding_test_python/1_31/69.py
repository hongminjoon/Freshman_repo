#https://school.programmers.co.kr/learn/courses/30/lessons/155652

def solution(s, skip, index):
    answer = ''
    origin_index = index
    
    for char in s:
        ord_char = ord(char)

        while index > 0:
            ord_char = (ord_char - ord('a') + 1) % 26 + ord('a')
            if chr(ord_char) in skip:
                index += 1
            index -= 1

        after_char = chr(ord_char)
        answer += after_char
        index = origin_index
        
    return answer




print(solution("aaaaa", "bcd", 1))
