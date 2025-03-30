# https://www.acmicpc.net/problem/10773
def solution(k):
    stack = []
    for _ in range(k):
        n = int(input())
        if n == 0:
            stack.pop()
        else:
            stack.append(n)

    return sum(stack)


k = int(input())
print(solution(k))