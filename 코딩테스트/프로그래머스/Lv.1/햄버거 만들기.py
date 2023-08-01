# https://school.programmers.co.kr/learn/courses/30/lessons/133502
def solution(ingredient):
    res = 0
    tmp = []
    for x in ingredient:
        tmp.append(x)
        if tmp[-4:] == [1,2,3,1]:
            res += 1
            for _ in range(4):
                tmp.pop()
    return res