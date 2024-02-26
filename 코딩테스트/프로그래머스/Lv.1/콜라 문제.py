# https://school.programmers.co.kr/learn/courses/30/lessons/132267
def solution(a, b, n):
    answer = 0
    while n >= a:
        remain_coke = n%a
        return_coke = n//a*b
        answer += return_coke
        n = remain_coke + return_coke
    return answer