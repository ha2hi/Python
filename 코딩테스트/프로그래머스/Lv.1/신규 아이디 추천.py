# https://school.programmers.co.kr/learn/courses/30/lessons/72410
import re
def solution(new_id):
    res = new_id.lower()
    res = re.sub('[^a-z0-9\-_.]', '', res)
    res = re.sub('\.{2,}', '.', res)
    res = re.sub('^[.]|[.]$', '', res)
    res = 'a' if len(res) == 0 else res[:15]
    res = re.sub('[.]$', '', res)
    res = res if len(res) > 2 else res + "".join([res[-1] for i in range(3-len(res))])

    return res

new_id = "...!@BaT#*..y.abcdefghijklm"
solution(new_id)