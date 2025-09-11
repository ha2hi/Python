# https://www.acmicpc.net/problem/2295
import sys

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()

tmp = set()
for i in range(N):
    for j in range(N):
        tmp.add(arr[i]+arr[j])

for i in range(N-1,-1,-1):
    for j in range(N):
        if arr[i]-arr[j] in tmp:
            print(arr[i])
            sys.exit()
