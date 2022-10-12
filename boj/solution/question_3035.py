import sys
input = sys.stdin.readline
r, c, zr, zc = map(int, input().split())
d = [input().rstrip() for _ in range(r)]
result = []
temp = ["".join([i*zc for i in r]) for r in d]
for r in temp:
    for _ in range(zr):
        result.append(r)
print("\n".join(result))