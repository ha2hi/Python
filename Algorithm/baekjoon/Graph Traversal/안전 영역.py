# https://www.acmicpc.net/problem/2468
from collections import deque

n = int(input())
res = 0
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

max_h = max(map(max, board))

for x in range(max_h):
    check = [row[:] for row in board]    
    tmp = 0

    for i in range(n):
        for j in range(n):
            if check[i][j] > x:
                q = deque()
                tmp += 1
                q.append((i,j))
                check[i][j] = x
                
                while q:
                    xx, yy = q.popleft()
                    for k in range(4):
                        nx = xx+dx[k]
                        ny = yy+dy[k]
                        if 0<=nx<n and 0<=ny<n and check[nx][ny] > x:
                            q.append((nx,ny))
                            check[nx][ny] = x
    
    res = max(res, tmp)

print(res)
