# https://school.programmers.co.kr/learn/courses/30/lessons/135808
def solution(k, m, score):
    score.sort(reverse=True)
    tmp = []
    res = 0
    for x in score:
        if len(tmp) < m:
            tmp.append(x)
        if len(tmp) == m:
            res += min(tmp) * m
            tmp = []
    return res