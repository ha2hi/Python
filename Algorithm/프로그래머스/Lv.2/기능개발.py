# https://school.programmers.co.kr/learn/courses/30/lessons/42586
from collections import deque
def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    result = []
    loop = 0
    count = 0  
    while len(progresses)> 0:
        if (progresses[0] + loop*speeds[0]) >= 100: 
            progresses.popleft()
            speeds.popleft()
            count += 1
            
        else:
            if count > 0:
                result.append(count)
                count = 0
            loop += 1
    result.append(count)
    return result