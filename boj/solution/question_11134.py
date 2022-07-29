import sys
input = sys.stdin.readline
for i in range(int(input())):
    cookie, days = map(int, input().split())
    if cookie%days != 0:
        print((cookie//days)+1)
    else:
        print(cookie//days)
