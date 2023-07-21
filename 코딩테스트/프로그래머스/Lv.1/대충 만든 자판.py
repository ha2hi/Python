# https://school.programmers.co.kr/learn/courses/30/lessons/160586?language=python3
def solution(keymap, targets):
    dict_key = {}
    answer = []
    for keys in keymap:
        for idx, key in enumerate(keys):
            if key in dict_key:
                dict_key[key] = min(dict_key[key], idx+1)
            else:
                dict_key[key] = idx + 1

    for target in targets:
        cnt = 0
        for row in target:
            if row not in dict_key:
                cnt = -1
                break
            else:
                cnt += dict_key[row]
        answer.append(cnt)

    return answer