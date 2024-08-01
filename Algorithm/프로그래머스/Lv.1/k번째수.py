#https://school.programmers.co.kr/learn/courses/30/lessons/42748
def solution(array, commands):
    res = []
    length = len(commands)
    for i in range(length):
        x, y, z = commands[i]
        tmp = sorted(array[x-1:y])[z-1]
        res.append(tmp)
    return res