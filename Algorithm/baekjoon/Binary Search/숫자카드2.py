# https://www.acmicpc.net/problem/10816
from collections import defaultdict
N = int(input())
arr = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))
count = defaultdict(int)

for x in arr:
    count[x] += 1

for c in check:
    print(count[c], end = " ")
