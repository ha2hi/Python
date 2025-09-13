# https://www.acmicpc.net/problem/3151
N = int(input())
arr = list(map(int, input().split()))
res = 0
arr.sort()

for i in range(N-2):
    a = arr[i]
    lt, rt = i+1, N-1
    while lt < rt:
        tmp = a+arr[lt]+arr[rt]

        if tmp == 0:
            if arr[lt] == arr[rt]:
                diff = rt - lt + 1
                res += diff*(diff-1)//2
                break
            else:
                lt_cnt = 1
                while arr[lt] == arr[lt+1] and lt < rt:
                    lt_cnt += 1
                    lt += 1
                rt_cnt = 1
                while arr[rt] == arr[rt-1] and lt < rt:
                    rt_cnt +=1
                    rt -= 1
                
                res += lt_cnt*rt_cnt
                lt += 1
                rt -= 1

        elif tmp > 0:
            rt -= 1
        else:
            lt +=1
print(res)
