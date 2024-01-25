#https://school.programmers.co.kr/learn/courses/30/lessons/12901\

#윤년 : 2월 29일 까지 = 366일
def solution(a, b):
    calender = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 
            8:31, 9:30, 10:31, 11:30, 12:31}
    week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]

    days = b - 1
    for month in range(1,a):
        days += calender[month]
    
    return week[days%7]

print(solution(1, 2))