import sys
K, N, M = list(map(int, sys.stdin.readline().split()))
if K*N > M:
    print(K*N-M)
else:
    print(0)