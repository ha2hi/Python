# https://www.acmicpc.net/problem/13144
N = int(input())
arr = list(map(int, input().split()))
count = [0] * 100001
lt = 0
res = 0

for rt in range(N):
    while count[arr[rt]] > 0:
        count[arr[lt]] -= 1
        lt += 1
    
    count[arr[rt]] += 1
    res += (rt-lt+1)
print(res)
