import sys
n = int(sys.stdin.readline())
result = 0
raw = sorted(list(map(int, sys.stdin.readline().split())))
for i in range(len(raw)):
    result += sum(raw[:i+1])
print(result)

