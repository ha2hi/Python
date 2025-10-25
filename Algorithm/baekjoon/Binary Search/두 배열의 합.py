from collections import Counter

T = int(input().strip())
n = int(input().strip())
A = list(map(int, input().split()))
m = int(input().strip())
B = list(map(int, input().split()))
sumA = []
for i in range(n):
    s = 0
    for j in range(i, n):
        s += A[j]
        sumA.append(s)

sumB = []
for i in range(m):
    s = 0
    for j in range(i, m):
        s += B[j]
        sumB.append(s)

countA = Counter(sumA)

answer = 0
for sb in sumB:
    answer += countA[T - sb]

print(answer)
