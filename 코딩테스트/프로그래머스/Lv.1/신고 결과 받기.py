# https://school.programmers.co.kr/learn/courses/30/lessons/92334
from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    user = defaultdict(list)
    cnt = defaultdict(int)

    for r in report:
        a, b = r.split()
        user[a].append(b)
        cnt[b] += 1
    
    for i in id_list:
        result = 0
        for u in user[i]:
            if cnt[u] >= k:
                result += 1
        answer.append(result)
    return answer
