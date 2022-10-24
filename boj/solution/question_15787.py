import sys
input = sys.stdin.readline
n, m = map(int, input().split())
t = [0 for _ in range(n)]
for _ in range(m):
    p = list(map(int, input().split()))
    if p[0] == 1:
        c, i, x = p
        t[i-1] = t[i-1] | (1 << x-1)
    elif p[0] == 2:
        c, i, x = p
        t[i-1] = t[i-1] & ~(1 << x-1)
    elif p[0] == 3:
        c, i = p
        t[i-1] = t[i-1] << 1
        t[i-1] = t[i-1] & ~(1 << 20) 
    elif p[0] == 4:
        c, i = p
        t[i-1] = t[i-1] >> 1
print(len(set(t)))
