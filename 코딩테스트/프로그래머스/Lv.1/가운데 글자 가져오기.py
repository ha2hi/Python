# https://school.programmers.co.kr/learn/courses/30/lessons/12903
def solution(s):
    a = len(s)//2
    if len(s) % 2 == 1:
        return s[a]
    else:
        return s[a-1] + s[a]