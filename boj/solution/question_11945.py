import sys
input = sys.stdin.readline
N, M = map(int, input().split())
reverse = []
for i in range(N):
    reverse.append(input().rstrip()[::-1])
print("\n".join(map(str, reverse)))