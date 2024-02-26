# https://school.programmers.co.kr/learn/courses/30/lessons/12932
def solution(n):
    answer = []
    a = str(n)
    b = list(a)

    for data in range(1,len(b)+1):
        answer.append(int(b[-data]))
        
    return answer