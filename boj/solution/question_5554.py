import sys
input = sys.stdin.readline
result = 0
for i in range(4):
    result += int(input())
print("\n".join(map(str, divmod(result, 60))))