# https://www.acmicpc.net/problem/20922
from collections import defaultdict
N, K = map(int, input().split())
arr = list(map(int, input().split()))
cur = defaultdict(int)
res = 1
lt = 0

for rt in range(N):
    cur[arr[rt]] += 1
    
    while cur[arr[rt]] > K:
        cur[arr[lt]] -= 1
        lt += 1
    res = max(res, rt-lt+1)
print(res)
