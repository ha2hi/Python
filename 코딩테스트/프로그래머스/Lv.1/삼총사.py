# https://school.programmers.co.kr/learn/courses/30/lessons/131705
from itertools import combinations
def solution(number):
    res = 0
    for combination in combinations(number,3): 
        if sum(combination) == 0:
            res += 1
    return res