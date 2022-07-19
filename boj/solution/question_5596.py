import sys
A = sum(list(map(int, sys.stdin.readline().split())))
B = sum(list(map(int, sys.stdin.readline().split())))
print(max(A,B))