# https://school.programmers.co.kr/learn/courses/30/lessons/76501
def solution(absolutes, signs):
    res = 0
    for x, y in zip(absolutes, signs):
        if y is True:
            res += x
        else:
            res -= x
    return res