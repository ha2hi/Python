def Count(mid):
    cnt = 1
    tmp = a[0]
    for i in range(1,n):
        if a[i] - tmp >= mid:
            cnt += 1
            tmp = a[i]
    return cnt


n, c = map(int, input().split())
a = []
for _ in range(n):
    x = int(input())
    a.append(x)
a.sort()
res = 0
lt = 1
rt = max(a)
while lt <= rt:
    mid = (lt + rt) // 2
    count = Count(mid)
    if count >= mid:
        res = max(res, mid)
        lt = mid + 1
    else:
        rt = mid - 1
print(res)
