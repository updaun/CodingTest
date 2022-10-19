import sys
input = sys.stdin.readline

g = input().rstrip()
result = []
for _ in range(int(input())):
    t = input().rstrip()
    temp = True
    for i, s in enumerate(g):
        if s != "*":
            if s != t[i]:
                temp = False
                break
    if temp:
        result.append(t)
print(len(result))
print(*result, sep="\n")