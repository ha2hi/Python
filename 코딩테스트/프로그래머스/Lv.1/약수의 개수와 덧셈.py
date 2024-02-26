# https://school.programmers.co.kr/learn/courses/30/lessons/77884
def solution(left, right):
    res = 0 
    for x in range(left, right+1):
        if int(x**0.5) == x **0.5:
            res -= x
        else:
            res += x
    return res
