# 백준
# 인사성 밝은 곰곰이
# https://www.acmicpc.net/problem/25192

# 시간초과
import sys
n = int(sys.stdin.readline())
entry = []
count = 0
for i in range(n):
    row = sys.stdin.readline().rstrip()
    if row == "ENTER":
        entry = []
        continue
    if row not in entry:
        entry.append(row)
        count += 1
print(count)

# 딕셔너리 사용
import sys
n = int(sys.stdin.readline())
entry = {}
count = 0
for i in range(n):
    row = sys.stdin.readline().rstrip()
    if row == "ENTER":
        entry = {}
        continue
    if row not in entry.keys():
        entry[row] = 1
        count += 1
print(count)


# 9
# ENTER
# pjshwa
# chansol
# chogahui05
# lms0806
# pichulia
# r4pidstart
# swoon
# tony9402

# 8

# 7
# ENTER
# pjshwa
# chansol
# chogahui05
# ENTER
# pjshwa
# chansol

# 5


# 3
# ENTER
# lms0806
# lms0806

# 1