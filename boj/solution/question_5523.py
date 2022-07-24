import sys
input = sys.stdin.readline
a_point = 0
b_point = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    if a > b:
        a_point += 1
    elif a < b:
        b_point += 1
print(a_point,b_point)