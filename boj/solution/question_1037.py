import sys
n = int(sys.stdin.readline())
d_list = sorted(list(map(int, sys.stdin.readline().split())))
if n == 1:
    print(d_list[0]**2)
else:
    print(d_list[0]*d_list[-1])
