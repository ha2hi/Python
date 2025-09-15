# https://www.acmicpc.net/problem/1477
def check(mid):
    cnt = 0
    for i in range(1, len(arr)):
        dis = arr[i] - arr[i-1]
        cnt += (dis-1) // mid

    return cnt

N, M, L = map(int, input().split())
arr = list(map(int, input().split()))
arr += [0,L]
arr.sort()
lt, rt = 1, L

while lt <= rt:
    mid = (lt+rt) // 2
    if check(mid) <= M:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(res)
