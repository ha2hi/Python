# https://school.programmers.co.kr/learn/courses/30/lessons/81301
def solution(s):
    a = {
    'zero' : 0,
    'one' : 1,
    'two' : 2,
    'three' : 3,
    'four' : 4,
    'five' : 5,
    'six' : 6,
    'seven' : 7,
    'eight' : 8,
    'nine' : 9
    }
    result = ""
    k = ""
    for i in s:
        if i.isdigit():
            result += i
        elif i.isalpha():
            k += i
            if k in a:
                result += str(a[k])
                k = ""
    return int(result)