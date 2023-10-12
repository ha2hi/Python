from collections import deque
max = 10000
ch = [0] * (max+1)
dis = [0] * (max+1)
n, m = map(int, input().split())
ch[n] = 1
dis[n] = 0
q = deque()
q.append(n)
while q:
    now = q.popleft()
    if now == m:
        break
    for next in (now-1, now+1, now+5):
        if 0<next<=max:
            if ch[next] == 0:
                q.append(next)
                ch[next] = 1
                dis[next] = dis[now] + 1
print(dis[m])
