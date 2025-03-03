# https://softeer.ai/practice/6288#pop_user
def max_value(W: int, bags: list):
    sorted_bags = sorted(bags, key = lambda x : x[1], reverse=True)
    res = 0
    for M, P in sorted_bags:
        if W == 0:
            break
        tmp = min(M, W)
        res += tmp * P
        W -= tmp
    
    return res


W, N = map(int, input().split())
bags = [list(map(int, input().split())) for _ in range(N)]
print(max_value(W, bags))