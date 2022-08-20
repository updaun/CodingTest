import sys
input = sys.stdin.readline
n = int(input())
num_list = list(map(int, input().split()))
d = [1] * n
for i in range(1, n):
    for j in range(i):
        if num_list[j] < num_list[i]:
            d[i] = max(d[i], d[j]+1)
print(max(d))