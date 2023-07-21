# https://school.programmers.co.kr/learn/courses/30/lessons/155652
def solution(s, skip, index):
    skip = set(skip)
    result = ''
    for x in s:
        cnt = 0
        ord_x = ord(x)
        while cnt != index:
            new_x = ord_x + 1
            if new_x > 122:
                new_x = 97
            if chr(new_x) not in skip:
                cnt += 1
                ord_x = new_x
            else:
                ord_x = new_x
        result += chr(ord_x)
    return result