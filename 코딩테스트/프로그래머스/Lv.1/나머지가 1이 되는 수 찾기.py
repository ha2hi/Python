# https://school.programmers.co.kr/learn/courses/30/lessons/87389
def solution(n):
    result = 0
    if n >= 3:
        for i in range(1, n+1):
            if n % i == 1:
                result = i
                break
                
        return result