def DFS(L,s):
    global res
    if L == m:
        sum = 0
        for j in range(len(house)):
            x1 = house[j][0]
            y1 = house[j][1]
            dis = 21470000
            for x in cb:
                x2 = pizza[x][0]
                y2 = pizza[x][1]
                dis = min(dis, abs(x1-x2) + abs(y1-y2))
            sum += dis
        res = min(res, sum)
    else:
        for i in range(s, len(pizza)):
            cb[L] = i 
            DFS(L+1, i+1)


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
house = []
pizza = []
cb = [0] * m
res = 2147000000
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            house.append((i,j))
        if a[i][j] == 0:
            pizza.append((i,j))
DFS(0,0)
print(res)
