# https://www.acmicpc.net/problem/16401
def check(mid):
    tmp = 0
    for x in snack:
        tmp += x//mid
    
    return tmp

M, N = map(int, input().split())
snack = list(map(int, input().split()))
lt = 1
rt = max(snack)
res = 0

while lt <= rt:
    mid = (lt+rt) // 2
    if check(mid) >= M:
        res = max(res, mid)
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
