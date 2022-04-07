import sys
n = int(sys.stdin.readline())
coordinate_list = []
for i in range(n):
    coordinate_list.append(list(map(int, sys.stdin.readline().split())))
coordinate_sorted = sorted(coordinate_list, key = lambda x:(x[0], x[1]))
for a,b in coordinate_sorted:
    print(a,b)