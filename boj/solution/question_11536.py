import sys
input = sys.stdin.readline
n =  int(input())
name_list = []
for i in range(n):
    name_list.append(input().rstrip())
if name_list == sorted(name_list):
    print("INCREASING")
elif name_list == sorted(name_list, reverse=True):
    print("DECREASING")
else:
    print("NEITHER")