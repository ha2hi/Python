# https://school.programmers.co.kr/learn/courses/30/lessons/118666
def solution(survey, choices):
    res = ''
    score = {'R' : 0, 'T' :0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    for survey, choice in zip(survey, choices):
        if choice > 4:
            score[survey[1]] += choice - 4
        elif choice < 4:
            score[survey[0]] += 4-choice
    if score['R'] >= score['T']:
        res += 'R'
    else:
        res += 'T'
    if score['C'] >= score['F']:
        res += 'C'
    else:
        res += 'F'
    if score['J'] >= score['M']:
        res += 'J'
    else:
        res += 'M'
    if score['A'] >= score['N']:
        res += 'A'
    else:
        res += 'N'
    return res