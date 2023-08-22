# https://school.programmers.co.kr/learn/courses/30/lessons/42889
def solution(N, stages):
    now_len = len(stages)
    res = {}
    for i in range(1, N+1):
        if now_len != 0:
            res[i] = stages.count(i) / now_len
            now_len -= stages.count(i)
        else:
            res[i] = 0
    return sorted(res, key = lambda x : res[x], reverse=True)