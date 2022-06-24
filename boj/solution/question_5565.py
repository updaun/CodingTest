import sys
value = int(sys.stdin.readline())
for i in range(9):
    value -= int(sys.stdin.readline())
print(value)