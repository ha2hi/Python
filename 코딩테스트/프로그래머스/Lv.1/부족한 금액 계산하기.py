# https://school.programmers.co.kr/learn/courses/30/lessons/82612
def solution(price, money, count):
    result = 0
    for i in range(1,count+1):
        result += price * i
        
    if money >= result:
        return 0 
    return abs(money - result)