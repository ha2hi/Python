def DFS(v, sum):
    global res
    if v == n:
        if 0<sum<=s:
            res.add(sum)
    else:
        DFS(v+1, sum+a[v])
        DFS(v+1, sum-a[v])
        DFS(V+1, sum)
        
n = int(input())
a = list(map(int, input().split()))
s = sum(a)
res = set()
DFS(0,0)
print(s-len(res))
