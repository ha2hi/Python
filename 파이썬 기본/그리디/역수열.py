n = int(input())
a = list(map(int, input().split()))
res = [0] * n
for i in range(n):
    for j in range(n):
        if a[i] == 0 and res[j] ==0:
            res[j] = i+1
            break
        elif res[j] == 0:
            a[i] -= 1
print(*res)
