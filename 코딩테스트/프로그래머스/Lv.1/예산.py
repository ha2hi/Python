# https://school.programmers.co.kr/learn/courses/30/lessons/12982
def solution(d, budget):
    d.sort()
    total = 0
    result = 0
    for i in d:
        total += i
        if total <= budget:
            result += 1
    return result