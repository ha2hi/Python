# https://school.programmers.co.kr/learn/courses/30/lessons/160586?language=python3
def solution(keymap, targets):
    result = []
    dict_key = {}
    for keys in keymap:
        for idx, key in enumerate(keys):
            if key in dict_key:
                dict_key[key] = min(dict_key[key], idx+1)
            else:
                dict_key[key] = idx+1
    for target in targets:
        tmp = 0
        for row in target:
            if row not in dict_key:
                result.append(-1)
                break
            tmp += dict_key[row]
        if row in dict_key:
            result.append(tmp)
    return result