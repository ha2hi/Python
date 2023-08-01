# https://school.programmers.co.kr/learn/courses/30/lessons/138477
def solution(k, score):
    tmp = []
    answer = []
    for row in score:
        tmp.append(row)
        tmp = sorted(tmp, reverse=True)[:k]
        answer.append(min(tmp))
    return answer