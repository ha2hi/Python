# https://school.programmers.co.kr/learn/courses/30/lessons/1845
def solution(nums):
    length = len(nums)//2
    nums = list(set(nums))
    count = 0
    for i in nums:
        if count < length:
            count += 1
            
    return count