# https://school.programmers.co.kr/learn/courses/30/lessons/12943
def solution(num):
    count = 0
    while num != 1:
        if count >= 500:
            return -1
        else:
            if num % 2 == 0:
                num //= 2
                count += 1

            elif num % 2 == 1:
                num = num*3+1
                count +=1
    return count