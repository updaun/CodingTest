import sys
T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    print(sum(list(map(int, sys.stdin.readline().split()))))