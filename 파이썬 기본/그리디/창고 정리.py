L = int(input())
a = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    a.sort()
    a[0] += 1
    a[-1] -= 1
print(max(a) - min(a))
