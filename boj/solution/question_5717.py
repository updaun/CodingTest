import sys
while True:
    m, f = list(map(int, sys.stdin.readline().split()))
    if m == 0 and f == 0:
        break
    print(m+f)