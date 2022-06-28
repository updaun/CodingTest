import sys
n = int(sys.stdin.readline())
for i in range(n):
    V, E = list(map(int, sys.stdin.readline().split()))
    print(2+E-V)