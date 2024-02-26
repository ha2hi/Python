# https://school.programmers.co.kr/learn/courses/30/lessons/81301
def solution(s):
    count_mapping = {"zero" : "0", "one" : "1", "two" : "2", "three" : "3", "four":"4", "five":"5", "six":"6","seven":"7","eight":"8","nine":"9"}
    for key, value in count_mapping.items():
        if key in s:
            s = s.replace(key, value)
    return int(s)