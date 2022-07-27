import sys
input = sys.stdin.readline
for i in range(int(input())):
    x, y = map(int, input().split())
    print(y-(x-y), x-y)