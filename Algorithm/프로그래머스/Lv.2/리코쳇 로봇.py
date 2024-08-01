# https://school.programmers.co.kr/learn/courses/30/lessons/169199?language=python3
from collections import deque
def solution(board):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    r, c = len(board), len(board[0])
    q = deque()
    distance = [[2147000000 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'R':
                q.append((i,j,0))
                distance[i][j] = 0
            if board[i][j] == 'G':
                res_x, res_y = i,j
    while q:
        now_x, now_y, cnt = q.popleft()
        if now_x == res_x and now_y == res_y:
            return cnt

        for i in range(4):
            xx, yy = now_x, now_y
            while 0<=xx+dx[i]<r and 0<=yy+dy[i]<c and board[xx+dx[i]][yy+dy[i]] != 'D':
                xx += dx[i]
                yy += dy[i]

            if distance[xx][yy] > cnt+1:
                distance[xx][yy] = cnt+1
                q.append((xx,yy,cnt+1))

    return -1
