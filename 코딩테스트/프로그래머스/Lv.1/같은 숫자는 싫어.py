# https://school.programmers.co.kr/learn/courses/30/lessons/12906
def solution(s):
    result = []
    for i in s:
        if result[-1:] == [i]: 
            continue
        result.append(i)
    return result