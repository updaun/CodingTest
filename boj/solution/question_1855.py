import sys
input = sys.stdin.readline
n = int(input())
s = input().rstrip()

temp = 0
s_list = []
while len(s) > 0:
    if temp % 2 == 1:
        s_list.append(s[:n][::-1])
    else:
        s_list.append(s[:n])
    s = s[n:]
    temp += 1

result = ''
for i in range(n):
    for s in s_list:
        if len(s) > i:
            result += s[i]
print(result)
