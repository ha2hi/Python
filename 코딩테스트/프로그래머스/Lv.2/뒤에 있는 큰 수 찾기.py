# https://school.programmers.co.kr/learn/courses/30/lessons/154539
def solution(numbers):
    res = [-1] * len(numbers)
    stack = []
    for i in range(len(numbers)):
        while stack and numbers[i] > numbers[stack[-1]]:
            res[stack.pop()] = numbers[i]

        stack.append(i)
    return res
