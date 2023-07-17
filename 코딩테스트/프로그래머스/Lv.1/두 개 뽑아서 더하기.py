# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    result = [] 
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i] + numbers[j] not in result:
                result.append(numbers[i]+numbers[j])
    return sorted(result)