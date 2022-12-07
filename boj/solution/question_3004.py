n = int(input())
a, b = 1, 1
for i in range(1, n+1):
    a, b = min(a, b) + 1, max(a, b)
print(a*b)