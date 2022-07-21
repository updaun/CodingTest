import sys
input = sys.stdin.readline
chess = list(map(int, input().split()))
target = [1, 1, 2, 2, 2, 8]
print(" ".join(map(str, [target[i]-chess[i] for i in range(6)])))