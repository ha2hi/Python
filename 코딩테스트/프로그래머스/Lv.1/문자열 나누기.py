# https://school.programmers.co.kr/learn/courses/30/lessons/140108
def solution(s):
    cnt1 = cnt2 = 0
    answer = 0
    for row in s:
        if cnt1 == cnt2:
            answer += 1
            x = row
        
        if row == x:
            cnt1 += 1
        else:
            cnt2 += 1
    return answer