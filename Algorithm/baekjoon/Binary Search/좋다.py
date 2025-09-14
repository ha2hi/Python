# https://www.acmicpc.net/problem/1253
N = int(input())
arr = list(map(int, input().split()))
res = 0
arr.sort()
for i in range(N):
    target = arr[i]
    lt, rt = 0, N-1

    while lt < rt:
        if lt == i:
            lt += 1
            continue
        if rt == i:
            rt -= 1
            continue
        
        sum_val = arr[lt] + arr[rt]
        if sum_val == target:
            res += 1
            break
        elif sum_val < target:
            lt += 1
        else:
            rt -= 1
print(res)            
