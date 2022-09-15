import sys
input = sys.stdin.readline
for i in range(int(input())):
    n = int(input())
    d = [False] + [True] * n
    for i in range(2, n+1):
        for j in range(i, n+1, i):
            if d[j]:
                d[j] = False
            else:
                d[j] = True
    print(d.count(True))
        