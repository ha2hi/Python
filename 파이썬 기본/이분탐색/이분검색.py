n, m = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = n - 1
a.sort()
while lt <= rt:
    mid = (lt+rt) // 2
    if m > a[mid]:
        lt = mid + 1
    elif m < a[mid]:
        rt = mid - 1
    else:
        print(mid+1)
        break
