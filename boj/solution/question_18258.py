from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
q = deque([])

for i in range(n):
    s = input().rstrip()
    s_list = s.split()
    if len(s_list) == 1:
        if s_list[0] == "pop":
            if len(q) == 0:
                print(-1)
            else:
                print(q.popleft())
        elif s_list[0] == "size":
            print(len(q))
        elif s_list[0] == "empty":
            if len(q) == 0:
                print(1)
            else:
                print(0)
        elif s_list[0] == "front":
            if len(q) == 0:
                print(-1)
            else:
                print(q[0])
        elif s_list[0] == "back":
            if len(q) == 0:
                print(-1)
            else:
                print(q[-1])

    else:
        command, num = s_list[0], int(s_list[1])
        if command == "push":
            q.append(num)