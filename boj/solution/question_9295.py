import sys
n = int(sys.stdin.readline())
for i in range(1, n+1):
    print(f"Case {i}: {sum(list(map(int, sys.stdin.readline().split())))}")