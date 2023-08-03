# https://school.programmers.co.kr/learn/courses/30/lessons/131128
def solution(X, Y):
    tmp = ''
    for i in range(9,-1,-1):
        tmp += str(i) * min(X.count(str(i)), Y.count(str(i)))
    if tmp == '':
        return "-1"
    elif len(tmp) == tmp.count("0"):
        return "0"
    else:
        return tmp