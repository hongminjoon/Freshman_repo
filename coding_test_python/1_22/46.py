# https://school.programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []
    
    temp_list_arr1 = [change2binary(num, n) for num in arr1]
    temp_list_arr2 = [change2binary(num, n) for num in arr2]

    temp_list_arr1 = [''.join(' ' if bit == '0' else '#' for bit in binary_str) for binary_str in temp_list_arr1]
    temp_list_arr2 = [''.join(' ' if bit == '0' else '#' for bit in binary_str) for binary_str in temp_list_arr2]

    for i in range(n):
        temp = ''
        for j in range(len(temp_list_arr1)):
            if temp_list_arr1[i][j] == '#' or temp_list_arr2[i][j] == '#':
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)

    return answer

def change2binary(n, digit):
    num = ""

    while n > 0:
        num += str(n % 2)
        n //= 2
    
    return num[::-1].zfill(digit)

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))