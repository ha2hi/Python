# https://school.programmers.co.kr/learn/courses/30/lessons/86491
def solution(sizes):
    cal_x = []
    cal_y = []
    for size in sizes:
        size.sort()
        cal_x.append(size[0])
        cal_y.append(size[1])

    return max(cal_x) * max(cal_y)