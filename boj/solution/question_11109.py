import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    d, n, s, p = map(int, input().split())
    if d+p*n < n*s:
        print("parallelize")
    elif d+p*n > n*s:
        print("do not parallelize")
    else:
        print("does not matter")
