# https://school.programmers.co.kr/learn/courses/30/lessons/12982
def solution(d, budget):
    d.sort()
    tmp = 0
    res = 0
    for x in d:
        if tmp + x <= budget:
            res += 1
            tmp += x
    return res
