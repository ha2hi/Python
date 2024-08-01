# https://school.programmers.co.kr/learn/courses/30/lessons/68935
def solution(n):
    res = ''
    while n:
        res += str(n%3)
        n = n//3
    return int(res,3)