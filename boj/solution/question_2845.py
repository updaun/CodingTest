import sys
input = sys.stdin.readline
L, P = map(int, input().split())
print(" ".join(map(str, [i-L*P for i in list(map(int, input().split()))])))