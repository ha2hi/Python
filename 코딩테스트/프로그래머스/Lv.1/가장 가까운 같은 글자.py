# https://school.programmers.co.kr/learn/courses/30/lessons/142086
def solution(s):
    check_dict = {}
    answer = []
    for idx, x in enumerate(s):
        if x not in check_dict:
            answer.append(-1)
            check_dict[x] = idx
        elif x in check_dict:
            answer.append(idx - check_dict[x])
            check_dict[x] = idx
    return answer