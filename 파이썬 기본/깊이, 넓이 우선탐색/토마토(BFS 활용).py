from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]
m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dis = [[0] * m for _ in range(n)]
q = deque()
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            q.append((i,j))
while q:
    cur_x, cur_y = q.popleft()
    for i in range(4):
        xx = cur_x + dx[i]
        yy = cur_y + dy[i]
        if 0<=xx<n and 0<=yy<m and a[xx][yy] == 0:
            a[xx][yy] = 1
            dis[xx][yy] = dis[cur_x][cur_y] + 1
            q.append((xx,yy))

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            print(-1)
else:
    print(max(map(max, dis)))
