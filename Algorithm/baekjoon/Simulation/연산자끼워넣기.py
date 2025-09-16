# https://www.acmicpc.net/problem/14888
N = int(input())
A = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split())

max_result = float('-inf')
min_result = float('inf')

def dfs(i, value, plus, minus, multiply, divide):
    global max_result, min_result
    if i == N:
        max_result = max(max_result, value)
        min_result = min(min_result, value)
        return
    
    if plus > 0:
        dfs(i+1, value + A[i], plus-1, minus, multiply, divide)
    if minus > 0:
        dfs(i+1, value - A[i], plus, minus-1, multiply, divide)
    if multiply > 0:
        dfs(i+1, value * A[i], plus, minus, multiply-1, divide)
    if divide > 0:
        if value < 0:
            dfs(i+1, -(-value // A[i]), plus, minus, multiply, divide-1)
        else:
            dfs(i+1, value // A[i], plus, minus, multiply, divide-1)

dfs(1, A[0], plus, minus, multiply, divide)
print(max_result)
print(min_result)
