import sys
input = sys.stdin.readline
n = int(input())
n_list = [int(input()) for i in range(n)]
print("\n".join(map(str, sorted(n_list, reverse=True))))
