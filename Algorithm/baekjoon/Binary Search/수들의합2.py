# https://www.acmicpc.net/problem/2003
N, M = map(int, input().split())
arr = list(map(int, input().split()))

res = 0
lt, rt = 0, 0
cur = arr[0]

while True:
    if cur == M:
        res += 1

    if cur >= M:
        cur -= arr[lt]
        lt += 1
    else:
        rt += 1
        if rt == N:
            break
        cur += arr[rt]

print(res)
