# https://school.programmers.co.kr/learn/courses/30/lessons/12921
def solution(n):
    data = set(range(2,n+1))
    
    for i in range(2, n+1):
        if i in data:
            data -= set(range(2 * i, n+1, i))
    return(len(data))