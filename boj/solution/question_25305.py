import sys
input = sys.stdin.readline
N, k = map(int, input().split())
print(sorted(list(map(int, input().split())), reverse=True)[k-1])