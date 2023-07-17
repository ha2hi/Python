# https://school.programmers.co.kr/learn/courses/30/lessons/86491
def solution(sizes):
    left = []
    right = []
    for i in range(len(sizes)):
        sizes[i].sort()
        left.append(sizes[i][0])
        right.append(sizes[i][1])
    return max(left) * max(right)