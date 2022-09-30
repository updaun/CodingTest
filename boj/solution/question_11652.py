import sys
input = sys.stdin.readline
n = int(input())
n_dict = dict()
for i in range(n):
    num = int(input())
    if num in n_dict.keys():
        n_dict[num] += 1
    else:
        n_dict[num] = 1
n_dict = sorted(n_dict, key=lambda x:(n_dict[x], -x))
print(n_dict[-1])