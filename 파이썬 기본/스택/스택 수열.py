# https://www.acmicpc.net/problem/1874
def solution(n):
    stack = []
    res = []
    i = 1
    for _ in range(n):
        k = int(input())
        while i <= k:
            stack.append(i)
            i += 1
            res.append('+')
        
        if stack[-1] == k:
            res.append('-')
            stack.pop()
        else:
            print("NO")
            return

    print(*res, sep="\n")

n = int(input())
solution(n)