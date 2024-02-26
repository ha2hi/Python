# https://school.programmers.co.kr/learn/courses/30/lessons/176963
def solution(name, yearning, photo):
    photo_len = len(photo)
    answer = [0] * photo_len

    score = dict(zip(name, yearning))

    for i in range(photo_len):
        for v in photo[i]:
            if v in score:
                answer[i] += score[v]

    return answer