# https://school.programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    a1 = [1,2,3,4,5]
    a2 = [2,1,2,3,2,4,2,5]
    a3 = [3,3,1,1,2,2,4,4,5,5]
    c1,c2,c3 = 0,0,0
    
    for i in range(len(answers)):
        s1 = i % 5
        s2 = i % 8
        s3 = i % 10
        
        if a1[s1] == answers[i]:
            c1 += 1
        if a2[s2] == answers[i]:
            c2 += 1
        if a3[s3] == answers[i]:
            c3 += 1
    
    k = max(c1,c2,c3)
    result = []
    if k == c1:
        result.append(1)
    if k == c2:
        result.append(2)
    if k == c3:
        result.append(3)
    
    return result