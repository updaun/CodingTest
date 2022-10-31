import sys
input = sys.stdin.readline
n = int(input())
n_list = [0]
temp = 0
for i in list(map(int, input().split())):
    n_list.append(temp+i)
    temp += i
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(n_list[b]-n_list[a-1])