# https://school.programmers.co.kr/learn/courses/30/lessons/133499
def solution(babbling):
    answer = 0
    for x in babbling:
        for val in ['aya', 'ye', 'woo', 'ma']:
            if val * 2 not in x:
                x = x.replace(val, ' ')
        if len(x.strip()) == 0:
            answer += 1
    return answer