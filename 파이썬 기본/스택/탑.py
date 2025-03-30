# https://www.acmicpc.net/problem/2493
def solution(n, tops):
    res = [0] * n
    stack = []

    for i in range(n):
        while stack and stack[-1][0] < tops[i]:
            stack.pop()
        
        if stack:
            res[i] = stack[-1][1] + 1
        
        stack.append((tops[i], i))

    print(*res)

n = int(input())
tops = list(map(int, input().split()))

solution(n, tops)