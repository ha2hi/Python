# https://www.acmicpc.net/problem/18869
from collections import Counter
M, N = map(int, input().split())
arrs = [list(map(int, input().split())) for _ in range(M)]
rank_arr = []
res = 0

for arr in arrs:
    uniq_sorted = sorted(set(arr))
    mapping = {v:i for i, v in enumerate(uniq_sorted)}
    rank_arr.append(tuple(mapping[x] for x in arr))

counter_rank = Counter(rank_arr)
for x in counter_rank.values():
    res += x * (x-1) // 2

print(res)
