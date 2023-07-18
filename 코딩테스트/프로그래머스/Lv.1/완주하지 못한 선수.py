# https://school.programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion):
    a = {}
    b = 0
    for data in participant:
        a[hash(data)] = data
        b += hash(data)
     
    for data in completion:
        b -= hash(data)
    
    answer = a[b] 
    return answer