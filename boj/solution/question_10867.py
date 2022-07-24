import sys
input = sys.stdin.readline
n = int(input())
print(" ".join(map(str, sorted(list(set(list(map(int, input().split()))))))))