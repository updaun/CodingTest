import sys
input = sys.stdin.readline
n, k = map(int, input().split())
n_list = list(map(int, input().split(",")))
for i in range(k):
    temp = [0]*(len(n_list)-1)
    for i in range(1, len(n_list)):
        temp[i-1] = n_list[i]-n_list[i-1]
    n_list = temp
print(*n_list, sep=",")