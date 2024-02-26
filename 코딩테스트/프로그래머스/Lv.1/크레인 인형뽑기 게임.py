# https://school.programmers.co.kr/learn/courses/30/lessons/64061
def solution(board, moves):
    board_len = len(board)
    tmp = []
    res = 0
    for move in moves:
        for i in range(board_len):
            if board[i][move-1] != 0:
                tmp.append(board[i][move-1])
                board[i][move-1] = 0
                break
        if len(tmp) >= 2 and tmp[-1] == tmp[-2]:
            res += 2
            tmp.pop()
            tmp.pop()
    return res