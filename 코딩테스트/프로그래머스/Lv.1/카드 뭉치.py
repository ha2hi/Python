# https://school.programmers.co.kr/learn/courses/30/lessons/159994
from collections import deque
def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)
    while goal:
        if len(cards1) >= 1 and goal[0] == cards1[0]:
            goal.popleft()
            cards1.popleft()
        elif len(cards2) >= 1 and goal[0] == cards2[0]:
            goal.popleft()
            cards2.popleft()
        else:
            return "No"
    return "Yes"