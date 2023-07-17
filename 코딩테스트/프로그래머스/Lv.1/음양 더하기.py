# https://school.programmers.co.kr/learn/courses/30/lessons/76501
def solution(absolutes, signs):
    answer = 0
    for absolute,sign in zip(absolutes, signs):
        if sign == True:
            answer += absolute
        else:
            answer -= absolute
    return answer