import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    s = input().rstrip()
    d = int(len(s)**0.5)
    temp = []
    for i in range(0, len(s), d):
        temp.append([i for i in s[i:i+d]])
    result = ''
    for i in range(d-1, -1, -1):
        for j in range(0, d):
            result += temp[j][i]
    print(result)