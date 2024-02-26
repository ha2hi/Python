def DFS(v, h1,h2,h3):
    global res
    if v == n:
        if h1 != h2 and h1 != h3 and h2 != h3:
            res = min(res, max(h1,h2,h3) - min(h1,h2,h3))
    else:
        DFS(v+1, h1+a[v], h2, h3)
        DFS(v+1, h1, h2+a[v], h3)
        DFS(v+1, h1, h2, h3+a[v])

n = int(input())
a = []
for _ in range(n):
    x = int(input())
    a.append(x)
res = 2147000000
DFS(0,0,0,0)
print(res)
