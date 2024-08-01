# https://school.programmers.co.kr/learn/courses/30/lessons/12917
def solution(s):
    answer = ''
    ls = list(s)
    ls.sort(reverse= True)
    answer = answer.join(ls)
    return answer