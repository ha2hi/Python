s = input()
digit = int("".join([row for row in s if row.isdigit()]))
print(digit)
cnt = 0
for x in range(1, digit+1):
    if digit % x == 0:
        cnt += 1
print(cnt)
