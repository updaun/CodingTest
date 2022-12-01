import sys
s = input()
l = len(s)
for i in range(1, l):
    a, b = s[:i], s[i:]
    temp_a, temp_b = 1, 1
    for c in a:
        temp_a *= int(c)
    for d in b:
        temp_b *= int(d)
    if temp_a == temp_b:
        print("YES")
        sys.exit(0)
else:
    print("NO")