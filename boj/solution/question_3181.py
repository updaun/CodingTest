import sys
input = sys.stdin.readline
ban_list = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
s = input().split()
result = s[0][0].upper()
for i in range(1, len(s)):
    if s[i] not in ban_list:
        result += s[i][0].upper()
print(result)