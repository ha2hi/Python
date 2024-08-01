# https://school.programmers.co.kr/learn/challenges?order=recent&levels=1&languages=python3&page=3
from itertools import combinations
def is_prime_number(num):
    if num == 0 or num == 1:
        return False
    else:
        for i in range(2,(num//2)+1):
            if num % i == 0:
                return False
        return True
    
def solution(nums):
    k = list(combinations(nums,3))
    count = 0
    for i in k:
        if is_prime_number(sum(i)):
            count += 1
    return count