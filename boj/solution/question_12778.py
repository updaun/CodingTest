import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, m = input().split()
    if m == 'C':
        print(*[ord(i)-64 for i in input().split()])
    else:
        print(*[chr(int(i)+64) for i in input().split()])