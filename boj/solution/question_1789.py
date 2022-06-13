import sys
target = int(sys.stdin.readline())
n = 1
while target*2 > n*(n+1):
    n += 1
if target*2 == n*(n+1):
    print(n)
else:
    print(n-1)