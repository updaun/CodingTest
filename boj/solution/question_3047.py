import sys
input = sys.stdin.readline
num_list = sorted(list(map(int, input().split())))
print(" ".join(map(str, [num_list[["A","B","C"].index(s)] for s in input().rstrip()])))