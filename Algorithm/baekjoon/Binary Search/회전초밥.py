# https://www.acmicpc.net/problem/2531
from collections import defaultdict
N, d, k, c = map(int, input().split())
arr = []
res = 0
for _ in range(N):
    arr.append(int(input()))

arr = arr + arr
cur = defaultdict(int)
for i in range(k):
    cur[arr[i]] += 1
res = len(cur) + (0 if c in cur else 1)

for i in range(1, N):
    cur[arr[i-1]] -= 1
    if cur[arr[i-1]] == 0:
        del cur[arr[i-1]]
    
    cur[arr[i+k-1]] += 1
    res = max(res, len(cur) + (0 if c in cur else 1))

print(res)
