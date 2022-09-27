import sys
input = sys.stdin.readline
n, k = map(int, input().split())
result = []
temp = 2
i = 1
while n >= temp*i:
    while n >= temp*i:
        if temp*i not in result:
            result.append(temp*i)
        i += 1
        if len(result) == k:
            break
    temp += 1
    i = 1
print(result[k-1])