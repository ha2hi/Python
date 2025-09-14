# https://www.acmicpc.net/problem/2110
def check(mid):
    count = 1
    last = arr[0]
    for i in range(1, N):
        if arr[i] - last >= mid:
            count += 1
            last = arr[i]
    
    return count

N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]
res = 0
lt = 1
rt = max(arr)
arr.sort()

while lt <= rt:
    mid = (lt+rt)//2
    if check(mid) >= C:
        res = max(res, mid)
        lt = mid+1
    else:
        rt = mid-1

print(res)
