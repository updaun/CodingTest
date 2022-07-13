import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    print(sum(list(map(int, input().split(',')))))