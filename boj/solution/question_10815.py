import sys
r1 = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
r2 = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
result = ''
inter = set(a).intersection(set(b))
result = ' '.join(map(str, [int(i in inter) for i in b]))
print(result)
