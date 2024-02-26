# https://school.programmers.co.kr/learn/courses/30/lessons/12916
def solution(s):
    p_count = 0
    y_count = 0
    for i in s:
        if i in("p", "P"):
            p_count +=1
        elif i in("y","Y"):
            y_count += 1
        
    if p_count == y_count:
        return True
    else:
        return False