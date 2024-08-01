# https://school.programmers.co.kr/learn/courses/30/lessons/154538
def solution(x, y, n):
    cnt = 0
    s = set([x])
    while s:
        if y in s:
            return cnt
        tmp = set()
        for x in s:
            if x+n <= y:
                tmp.add(x+n)
            if x*2 <= y:
                tmp.add(x*2)
            if x*3 <= y:
                tmp.add(x*3)
        s = tmp
        cnt += 1
    return -1
