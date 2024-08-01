n = int(input())
for idx in range(1,n+1):
    s = input().lower()
    if s == s[::-1]:
        print(f"#{idx} YES")
    else:
        print(f"#{idx} NO")
