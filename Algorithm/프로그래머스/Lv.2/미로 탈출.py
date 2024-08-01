# https://school.programmers.co.kr/learn/courses/30/lessons/159993
from collections import deque
def bfs(s, e, maps):
    dx = [0,1,-1,0]
    dy = [1,0,0,-1]

    q = deque()
    r = len(maps)
    c = len(maps[0])
    ch = [[False]*c for _ in range(r)]
    flag = False

    for i in range(r):
        if flag:
            break
        for j in range(c):
            if maps[i][j] == s:
                q.append((i,j,0))
                ch[i][j] = True
                flag = True 
                break
    while q:
        cur_x, cur_y, cnt = q.popleft()
        if maps[cur_x][cur_y] == e:
            return cnt
        for i in range(4):
            xx = cur_x + dx[i]
            yy = cur_y + dy[i]
            if 0<=xx<r and 0<=yy<c and maps[xx][yy] != 'X':
                if not ch[xx][yy]:
                    q.append((xx,yy, cnt+1))
                    ch[xx][yy] = True
    return -1

def solution(maps):
    path1 = bfs('S', 'L', maps)
    path2 = bfs('L', 'E', maps)
    if path1 != -1 and path2 != -1:
        return path1+path2
    return -1
