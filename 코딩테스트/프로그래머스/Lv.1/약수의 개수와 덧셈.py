# https://school.programmers.co.kr/learn/courses/30/lessons/77884
def solution(left, right):
    result = 0
    
    for  i in range(left, right + 1):
        count  = 0
        for j in range(1, i+1):
            if i % j == 0:
                
                count += 1
                
        if count % 2  == 0:
            result += i
        else:
            result -= i
    
    return result