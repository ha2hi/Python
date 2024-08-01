# https://school.programmers.co.kr/learn/courses/30/lessons/12950
def solution(arr1, arr2):
    return [list(map(sum, zip(*arr))) for arr in zip(arr1, arr2)]

