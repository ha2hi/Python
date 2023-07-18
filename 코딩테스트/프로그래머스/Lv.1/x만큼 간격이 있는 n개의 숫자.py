# https://school.programmers.co.kr/learn/courses/30/lessons/12954
def solution(x, n):
    answer = []
    for i in range(n):
        answer.append(x)
        x += answer[0]
    return answer 

def solution1(x, n):
    answer = []
    for j in range(1, n+1):
        answer.append(x*j)
    return answer