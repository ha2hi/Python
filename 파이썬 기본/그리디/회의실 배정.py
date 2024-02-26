n = int(input())
a = []
for _ in range(n):
    x, y = map(int, input().split())
    a.append((x,y))
a.sort(key=lambda x : (x[1],x[0]))
cnt = 1
e_e = a[0][1]
for i in range(1,n):
    if a[i][0] >= e_e:
        cnt += 1
        e_e = a[i][1]
print(cnt)
