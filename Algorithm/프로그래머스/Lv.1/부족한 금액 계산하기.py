# https://school.programmers.co.kr/learn/courses/30/lessons/82612
def solution(price, money, count):
    tmp = 0
    for i in range(1,count+1):
        tmp += price * i
    if money >= tmp:
        return 0
    else:
        return tmp-money