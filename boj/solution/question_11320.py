import sys
input = sys.stdin.readline
for i in range(int(input())):
    a, b = map(int, input().split())
    n = a // b
    result = 0
    for i in range(1, n+1):
        result += 2*i - 1
    print(result)