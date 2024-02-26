# https://school.programmers.co.kr/learn/courses/30/lessons/154540
from collections import deque
def solution(maps):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    r, c = len(maps), len(maps[0])
    res = []
    ch = [[0] * c for _ in range(r)]
    tmp = 0
    q = deque()
    for i in range(r):
        for j in range(c):
            if maps[i][j] != 'X' and ch[i][j] == 0:
                q.append((i,j))
                ch[i][j] = 1
                while q:
                    cur_x, cur_y = q.popleft()
                    tmp += int(maps[cur_x][cur_y])
                    for k in range(4):
                        xx = cur_x + dx[k]
                        yy = cur_y + dy[k]
                        if 0<=xx<r and 0<=yy<c and maps[xx][yy] != 'X' and ch[xx][yy] == 0:
                            q.append((xx,yy))
                            ch[xx][yy] = 1
                res.append(tmp)
                tmp = 0
    if res:
        return sorted(res)
    else:
        return [-1]
