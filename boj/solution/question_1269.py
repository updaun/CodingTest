import sys
N, M = list(map(int, sys.stdin.readline().split()))
A = set(map(int, sys.stdin.readline().split()))
B = set(map(int, sys.stdin.readline().split()))
print(len(A.difference(B).union(B.difference(A))))
