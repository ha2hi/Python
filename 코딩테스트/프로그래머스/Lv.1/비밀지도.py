# https://school.programmers.co.kr/learn/courses/30/lessons/17681
def solution(n, arr1, arr2):
    res = []
    for i in range(n):
        tmp = bin(arr1[i]|arr2[i])[2:].zfill(n)
        tmp = tmp.replace('0', " ")
        tmp = tmp.replace("1", "#")
        res.append(tmp)
    return res