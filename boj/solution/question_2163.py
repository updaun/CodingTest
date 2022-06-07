import sys
N, M = list(map(int, sys.stdin.readline().split()))
print(int(((N-1)+((N-1)*M)+(M-1)+((M-1)*N))/2))
# print(N*M-1)