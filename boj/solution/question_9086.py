import sys
input = sys.stdin.readline
for i in range(int(input())):
    s = input().rstrip()
    print(s[0]+s[-1])