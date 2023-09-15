import sys
input = sys.stdin.readline
stack = []
n = int(input())
for i in range(n):
    c = input().split()
    if c[0] == "1":
        stack.append(c[1])
    elif c[0] == "2":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif c[0] == "3":
        print(len(stack))
    elif c[0] == "4":
        print(1 if len(stack) == 0 else 0)
    elif c[0] == "5":
        if stack:
            print(stack[-1])
        else:
            print(-1)