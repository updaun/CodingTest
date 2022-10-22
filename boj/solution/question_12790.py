import sys
input = sys.stdin.readline
for _ in range(int(input())):
    s = list(map(int, input().split()))
    a, b, c, d = [s[i]+s[i+4] for i in range(4)]
    if a < 1:
        a = 1
    if b < 1:
        b = 1
    if c < 0:
        c = 0
    print(a + 5*b + 2*c + 2*d)