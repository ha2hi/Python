# https://www.acmicpc.net/problem/2467
import sys
N = int(input())
arr = list(map(int, input().split()))
if all(x>0 for x in arr):
    print(arr[0], arr[1])
    sys.exit()
elif all(x<0 for x in arr):
    print(arr[-2], arr[-1])
    sys.exit(0)

lt, rt = 0, N-1
res = [0]*2
res_value = float('inf')

while lt < rt:
    sum_val = arr[lt] + arr[rt]

    if abs(sum_val) < res_value:
        res_value = abs(sum_val)
        res = [arr[lt], arr[rt]]
    
    if sum_val < 0:
        lt += 1
    else:
        rt -= 1

print(*res)
