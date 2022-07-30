import sys
input = sys.stdin.readline
for i in range(int(input())):
    N, K = map(int, input().split())
    child = [i//K for i in list(map(int, input().split()))]
    print(sum(child))