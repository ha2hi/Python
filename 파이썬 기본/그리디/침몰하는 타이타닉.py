from collections import deque
n, m = map(int, input().split())
q = list(map(int, input().split()))
cnt = 0
q.sort()
a = deque(q)
while a:
    if len(a) > 1:
        if a[0] + a[-1] > m:
            cnt += 1
            a.pop()
        else:
            cnt += 1
            a.popleft()
            a.pop()
    else:
        cnt += 1
        break
print(cnt)
