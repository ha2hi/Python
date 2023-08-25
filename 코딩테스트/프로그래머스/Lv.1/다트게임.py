#https://school.programmers.co.kr/learn/courses/30/lessons/17682
def solution(dartResult):
    answer = []
    dartResult = dartResult.replace('10', 'A')
    bonus = {'S':1, 'D':2, 'T':3}
    for dart in dartResult:
        if dart.isdigit() or dart == 'A':
            answer.append(10 if dart=='A' else int(dart))
        elif dart.isalpha():
            answer[-1] **= bonus[dart]
        else:
            if dart == '*':
                if len(answer) < 2:
                    answer[-1] *= 2
                else:
                    answer[-1] *= 2
                    answer[-2] *= 2
            elif dart == '#':
                answer[-1] *= -1
                    
    return sum(answer)