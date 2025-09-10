# http://acmicpc.net/problem/1806
import sys
N, S = map(int, input().split())
arr = list(map(int, input().split()))
lt = 0
res = float('inf')
tmp = 0

if max(arr) >= S:
    print(1)
    sys.exit(0)
for rt in range(N):
    tmp += arr[rt]

    while tmp >= S:
        res = min(res, rt-lt+1)
        tmp -= arr[lt]
        lt += 1

if res == float('inf'):
    print(0)
else:
    print(res)
