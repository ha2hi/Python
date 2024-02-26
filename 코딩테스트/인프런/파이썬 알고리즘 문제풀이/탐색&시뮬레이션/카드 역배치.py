card = [i for i in range(1,21)]
for _ in range(10):
    lt, rt = map(int, input().split())
    while lt < rt:
        card[lt-1], card[rt-1] = card[rt-1], card[lt-1]
        lt += 1
        rt -= 1
print(*card)
