# https://school.programmers.co.kr/learn/courses/30/lessons/42889
def solution(N, stages):
    dic = {}
    player = len(stages)
    for i in range(1,N+1):
        if player != 0:
            count = stages.count(i)
            dic[i] = count/player
            player -= count
        else:
            dic[i] = 0
    
    return sorted(dic, key = lambda x : dic[x], reverse=True)