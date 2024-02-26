# https://school.programmers.co.kr/learn/courses/30/lessons/12948
def solution(phone_number):
    phone_len = len(phone_number) - 4
    return '*'*phone_len +phone_number[-4:]