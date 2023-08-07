# https://school.programmers.co.kr/learn/courses/30/lessons/77484
def solution(lottos, win_nums):
    res = []
    win_nums = set(win_nums)
    tmp = 0
    zero_count = 0
    rank = {6 : 1, 5 : 2, 4: 3, 3:4, 2:5, 1:6, 0:6}
    for lotto in lottos:
        if lotto in win_nums:
            tmp += 1
        if lotto == 0:
            zero_count += 1
    res.append(rank[tmp+zero_count])
    res.append(rank[tmp])
    return res