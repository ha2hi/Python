# https://school.programmers.co.kr/learn/courses/30/lessons/68935
def solution(n):
    rev_base = ""
    result = 0
    q = 3
    
    while n > 0:
        n, mod = divmod(n,q)
        rev_base += str(mod)
    rev_base = rev_base[::-1]
    
    for i in range(len(rev_base)):
        result += int(rev_base[i]) * (3 ** i)
    
    return result