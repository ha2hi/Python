# https://www.acmicpc.net/problem/18870
import bisect
N = int(input())
X = list(map(int, input().split()))
res = []
sorted_arr = sorted(set(X))

for i in range(N):
    print(bisect.bisect_left(sorted_arr, X[i]), end = " ")
