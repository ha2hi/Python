def DFS(v, sum):
    global res
    if sum > T:
        return
    if v == k:
        if sum == T:
            res += 1
    else:
        for i in range(a[v][1]+1):
            DFS(v+1, sum+(a[v][0] * i))

T = int(input())
k = int(input())
a = []
for _ in range(k):
    x, y = map(int,input().split())
    a.append((x,y))
res = 0
DFS(0,0)
print(res)
