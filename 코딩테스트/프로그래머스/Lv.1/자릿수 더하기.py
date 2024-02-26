# https://school.programmers.co.kr/learn/courses/30/lessons/12931
def solution(n):
    n = list(str(n))
    result = 0
    for i in n:
        result += int(i)
    return result