# https://school.programmers.co.kr/learn/courses/30/lessons/12947
def solution(x):
    y = list(str(x))

    result = 0
    for i in y:
        result += int(i)

    if x % result == 0:
        return True
    else:
        return False