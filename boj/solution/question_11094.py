import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    s = input().rstrip()
    if "Simon says" in s:
        print(s[10:])