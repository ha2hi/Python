# https://www.acmicpc.net/problem/2230
N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

lt, rt = 0, 1
res = float('inf')

while lt < N and rt < N:
    diff = arr[rt] - arr[lt]
    if diff >= M:
        res = min(res, diff)
        lt += 1
    else:
        rt += 1

print(res)
