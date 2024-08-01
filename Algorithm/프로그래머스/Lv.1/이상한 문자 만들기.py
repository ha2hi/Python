# https://school.programmers.co.kr/learn/courses/30/lessons/12930
def solution(s):
    s = s.split(" ")
    for i in range(len(s)):
        ls = list(s[i])
        for j in range(len(ls)):
            if j % 2 == 0:
                ls[j] = ls[j].upper()
            else:
                ls[j] = ls[j].lower()
                
        s[i] = "".join(ls)
    return " ".join(s)