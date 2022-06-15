import sys
a,b = list(map(int, sys.stdin.readline().split()))
while a != 0 and b != 0:
    if a>b:
        print("Yes")
    else:
        print("No")
    a,b = list(map(int, sys.stdin.readline().split()))
