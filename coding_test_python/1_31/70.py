#https://school.programmers.co.kr/learn/courses/30/lessons/250125

def solution(board, h, w):
    count = 0
    board_len = len(board)
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0 , -1]

    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]

        if 0 <= h_check < board_len and  0 <= w_check < board_len:
            if board[h][w] == board[h_check][w_check]:
                count += 1
    
    return count

solution([["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]], 1, 1)