import sys
input = sys.stdin.readline
total = int(input())
n = int(input())
result = 0
for i in range(n):
    price, count = map(int, input().split())
    result += price * count
if total == result:
    print("Yes")
else:
    print("No")

