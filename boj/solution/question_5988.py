import sys
input = sys.stdin.readline
for i in range(int(input())):
    s = input().split()
    if int(s[-1])%2 == 0:
        print("even")
    else:
        print("odd")