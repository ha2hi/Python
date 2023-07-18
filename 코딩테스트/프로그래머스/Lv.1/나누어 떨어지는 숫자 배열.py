# https://school.programmers.co.kr/learn/courses/30/lessons/12910
def solution(arr, divisor):
    result = []
    for i in arr:
        if i % divisor == 0:
            result.append(i)
            result.sort()
    if result == []:
        return [-1]
    return result