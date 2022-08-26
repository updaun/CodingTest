n = int(input())
d = [0 for i in range(n+2)]
d[2] = 3
for i in range(4, n+1, 2):
    d[i] = d[i-2]*3 + sum(d[:i-2])*2 + 2
print(d[n])