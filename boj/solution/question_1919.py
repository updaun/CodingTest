import sys
input = sys.stdin.readline
a = list(input().rstrip())
b = list(input().rstrip())
temp_b = b.copy()
i = []
for s in a:
    if s in temp_b:
        temp_b.remove(s)
        i.append(s)
print(len(a)+len(b)-(2*len(i)))