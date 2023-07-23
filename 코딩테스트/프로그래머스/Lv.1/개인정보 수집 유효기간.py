# https://school.programmers.co.kr/learn/courses/30/lessons/150370
def solution(today, terms, privacies):
    answer = []
    terms_dict = {}
    for item in terms:
        idx, val = item.split(' ')
        terms_dict[idx] = int(val)

    limit_year, limit_month, limit_day = list(map(int, today.split('.')))
    limit_month += limit_year*12
    limit_day += limit_month*28

    for idx, privacie in enumerate(privacies):
        cur_date, cur_term = privacie.split(' ')
        cur_year, cur_month, cur_day = list(map(int, cur_date.split('.')))
        cur_month += terms_dict[cur_term]
        cur_month += cur_year*12
        cur_day += cur_month*28
        if cur_day-1 < limit_day:
            answer.append(idx+1)

    return answer