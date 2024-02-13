#https://school.programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''

    key=[[1,2,3],
         [4,5,6],
         [7,8,9],
         ["*",0,"#"]]
    l,r="*","#"
    
    for number in numbers:
        if number in [1, 4, 7]:
            l = number
            answer += 'L'
        elif number in [3, 6, 9]:
            r = number
            answer += 'R'
        else:
            for i in range(4):
                for j in range(3):
                    if key[i][j]==number:
                        target=(i,j)
                    if key[i][j]==l:
                        l_curr =(i,j)
                    if key[i][j]==r:
                        r_curr=(i,j)
            
            l_dist = abs(target[0]-l_curr[0])+abs(target[1]-l_curr[1])
            r_dist = abs(target[0]-r_curr[0])+abs(target[1]-r_curr[1])

            if l_dist < r_dist:
                answer += 'L'
                l = number
            elif r_dist < l_dist:
                answer += 'R'
                r = number
            else:
                if hand == "left":
                    answer += 'L'
                    l = number 
                elif hand == "right":
                    answer += 'R'
                    r = number

    return answer

solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")