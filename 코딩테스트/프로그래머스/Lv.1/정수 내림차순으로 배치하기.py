# https://school.programmers.co.kr/learn/courses/30/lessons/12933
def solution(n):
    n = list(str(n))
    result = []
    for i in n:
        result.append(int(i))
    result.sort(reverse=True)
    
    a =''
    for i in result:
        a += str(i)
    
    return int(a)