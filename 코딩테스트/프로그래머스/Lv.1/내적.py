# https://school.programmers.co.kr/learn/courses/30/lessons/70128
def solution(a, b):
    answer = 0
    for data1 in range(len(a)):
        for data2 in range(len(b)):
            if data1 == data2:
                answer += a[data1] * b[data2]
    return answer