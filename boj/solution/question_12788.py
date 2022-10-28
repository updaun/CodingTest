import sys
input = sys.stdin.readline
n = int(input())
m, k = map(int, input().split())
temp = m*k
for i, p in enumerate(sorted(list(map(int, input().split())), reverse=True)):
    temp -= p
    if temp <= 0:
        print(i+1)
        break
else:
    print("STRESS")