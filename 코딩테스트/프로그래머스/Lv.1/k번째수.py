#https://school.programmers.co.kr/learn/courses/30/lessons/42748
def solution(array, commands):
    result = []
    for s in range(len(commands)):
        i, j, k = commands[s]
        a = sorted(array[i-1:j])
        result.append(a[k-1])
    return result