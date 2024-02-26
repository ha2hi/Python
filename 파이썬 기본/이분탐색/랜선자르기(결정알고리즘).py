def Count(mid):
    cnt = 0
    for row in a:
        cnt += row//mid
    return cnt

n, c = map(int, input().split())
a = []
for _ in range(n):
    x = int(input())
    a.append(x)
lt = 0
rt = max(a)
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    count = Count(mid)
    if count == c:
        res = max(res, mid)
        lt = mid + 1
    elif count > c:
        lt = mid + 1
    else:
        rt = mid - 1
print(res)
