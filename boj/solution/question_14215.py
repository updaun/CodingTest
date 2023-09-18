a, b, c = sorted(list(map(int, input().split())))
if a + b <= c:
    c = a+b-1
print(a+b+c)
