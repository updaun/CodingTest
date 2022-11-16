import sys
input = sys.stdin.readline
def cal(gram, price):
    return round(price / gram * 1000, 2)
y, x = map(int, input().split())
n = int(input())
result = [cal(x,y)]
for i in range(n):
    y, x = map(int, input().split())
    result.append(cal(x,y))
print(f"{min(result):.2f}")