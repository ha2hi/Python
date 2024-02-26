# https://school.programmers.co.kr/learn/courses/30/lessons/68644
from itertools import permutations
def solution(numbers):
    res = set()
    for x, y in permutations(numbers, 2):
        res.add(x+y)
    res = sorted(list(res))
    return res