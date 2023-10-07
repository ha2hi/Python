def DFS(x):
    if x > 1:
        DFS(x//2)
        print(x%2, end = " ")


if "__name__" == "__main__":
    n = int(input())
    DFS(n)