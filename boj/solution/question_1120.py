import sys
input = sys.stdin.readline
a, b = input().split()
result = []
for i in range(len(b)-len(a)+1):
    temp = 0
    for idx, s in enumerate(b[i:i+len(a)]):
        if a[idx] != s:
            temp += 1
    result.append(temp)
print(min(result))