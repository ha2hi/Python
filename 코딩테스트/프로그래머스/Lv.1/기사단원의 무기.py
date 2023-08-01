# https://school.programmers.co.kr/learn/courses/30/lessons/136798
def solution(number, limit, power):
    result = [1]
    for i in range(2, number+1):
        cnt = 0
        for j in range(1, int(i**(1/2)+1)):
            if i%j == 0:
                cnt += 1
                if j ** 2 != i:
                    cnt += 1
        if cnt > limit:
            result.append(power)
        else:
            result.append(cnt)
    return sum(result)