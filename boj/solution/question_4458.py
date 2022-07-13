import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    target = input().rstrip()
    print(target[0].upper()+target[1:])