def solution(board):
    strboard = ''.join(board)
    val = strboard.count('O') - strboard.count('X')
    if val not in set([0,1]):
        return 0
    colboard = list(zip(*board))
    o_cnt, x_cnt = 0, 0
    for i in range(3):
        if colboard[i].count('O') == 3 or board[i].count('O')==3:
            o_cnt += 1
        if colboard[i].count('X') == 3 or board[i].count('X')==3:
            x_cnt += 1

    for i in [0,2]:
        if board[0][i] == board[1][1] == board[2][2-i] == 'O':
            o_cnt += 1
        if board[0][i] == board[1][1] == board[2][2-i] == 'X':
            x_cnt += 1
    if o_cnt and x_cnt:
        return 0
    if o_cnt==1 and val==0:
        return 0
    if x_cnt==1 and val>=1:
        return 0
    return 1
