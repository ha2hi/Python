# https://school.programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    f_1 = [1,2,3,4,5]
    f_2 = [2,1,2,3,2,4,2,5]
    f_3 = [3,3,1,1,2,2,4,4,5,5]
    tmp = [0] * 3
    res = []
    
    for idx, answer in enumerate(answers):
        if answer == f_1[idx%5]:
            tmp[0] += 1
        if answer == f_2[idx%8]:
            tmp[1] += 1
        if answer == f_3[idx%10]:
            tmp[2] += 1

    for idx, x in enumerate(tmp):
        if x == max(tmp):
            res.append(idx+1)
    return res