# 백준
# 2485번 가로수
# https://www.acmicpc.net/problem/2485

import math
import sys

input = sys.stdin.readline
n = int(input())
n_list = [int(input()) for i in range(n)]

diff = []
for i in range(n-1):
    diff.append(n_list[i+1] - n_list[i])
set_diff = list(set(diff))

gcd = set_diff[0]
for i in set_diff:
    gcd = math.gcd(gcd, i)

answer = 0
for i in diff:
    answer += i // gcd - 1
print(answer)

# 4
# 1
# 3
# 7
# 13

# 3

# 4
# 2
# 6
# 12
# 18

# 5