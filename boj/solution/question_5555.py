import sys
input = sys.stdin.readline
target = input().rstrip()
result = 0
for i in range(int(input())):
    ring = input().rstrip()
    if target in ring*2:
        result += 1
print(result)