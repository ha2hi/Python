# https://www.acmicpc.net/problem/22862
S, K = map(int, input().split())
arr = list(map(int, input().split()))
lt = 0
res = 0
tmp = 0

for rt in range(S):
    tmp += arr[rt] % 2

    while tmp > K:
        tmp -= arr[lt] % 2
        lt += 1

    res = max(res, rt-lt+1-tmp)
print(res)
