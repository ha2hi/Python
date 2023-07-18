# https://school.programmers.co.kr/learn/courses/30/lessons/12926
def solution(s, n):
    ls = list(s)
    for c in range(len(ls)):
        if ls[c].isupper():
            ls[c] = chr((ord(ls[c]) - ord('A') + n) % 26 + ord('A'))
        elif ls[c].islower():
            ls[c] = chr((ord(ls[c]) - ord('a') + n) % 26 + ord('a'))
    return "".join(ls)