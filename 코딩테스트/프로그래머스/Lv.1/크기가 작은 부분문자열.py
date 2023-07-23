# https://school.programmers.co.kr/learn/courses/30/lessons/147355
def solution(t, p):
    answer = 0
    t_len = len(t)
    p_len = len(p)
    i = 0
    while t_len - i  >= p_len:
        if int(p) >= int(t[i:p_len+i]):
            answer += 1
        i += 1
    return answer