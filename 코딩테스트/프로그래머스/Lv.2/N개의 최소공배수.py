# https://school.programmers.co.kr/learn/courses/30/lessons/12953
def solution(arr):
    i = max(arr)
    while True:
        if all(i % x == 0 for x in arr):
            gcd = i
            break
        i += 1
        
    return i