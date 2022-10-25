import sys
input = sys.stdin.readline
def t(n):
    return n*(n+1)//2
for _ in range(int(input())):
    n = int(input())
    print(sum([k*t(k+1) for k in range(1, n+1)]))