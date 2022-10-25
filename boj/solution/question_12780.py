import sys
input = sys.stdin.readline
count = 0
h = input().rstrip()
n = input().rstrip()
temp = h.replace(n, "")
print((len(h)-len(temp))//len(n))