# https://school.programmers.co.kr/learn/courses/30/lessons/181188?language=python3#
def solution(targets):
    answer = 0
    targets.sort(key = lambda x : (x[1], x[0]))
    ep = 0
    for s,e in targets:
        if s >= ep:
            answer += 1
            ep = e
    return answer