#https://school.programmers.co.kr/learn/courses/30/lessons/161989#
from collections import deque
def solution(n, m, section):
    section = deque(section)
    cnt = 0
    while section:
        first_value = section.popleft()

        while section and section[0] - first_value < m:
            section.popleft()
        cnt += 1
    return cnt