from collections import deque
import sys

input = sys.stdin.readline
d = deque([])
n = int(input())
for c in range(n):
    c_list = list(map(int, input().split()))
    if len(c_list) == 2:
        command, num = c_list[0], c_list[1]
        if command == 1:
            d.appendleft(num)
        elif command == 2:
            d.append(num)
    elif len(c_list) == 1:
        command = c_list[0]
        if command == 3:
            if len(d) != 0:
                print(d.popleft())
            else:
                print(-1)
        elif command == 4:
            if len(d) != 0:
                print(d.pop())
            else:
                print(-1)
        elif command == 5:
            print(len(d))
        elif command == 6:
            if len(d) == 0:
                print(1)
            else:
                print(0)
        elif command == 7:
            if len(d) != 0:
                print(d[0])
            else:
                print(-1)
        elif command == 8:
            if len(d) != 0:
                print(d[-1])
            else:
                print(-1)

        