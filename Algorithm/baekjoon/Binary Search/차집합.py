# https://www.acmicpc.net/problem/1822
n_a, n_b = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = set(map(int, input().split()))
res = []
for a in arr_a:
    if a not in arr_b:
        res.append(a)
if res != []:
    print(len(res))
    print(*sorted(res))
else:
    print(0)
