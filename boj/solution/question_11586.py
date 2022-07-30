import sys
input = sys.stdin.readline
mirror = []
for i in range(int(input())):
    mirror.append(input().rstrip())
method = int(input())
if method == 2:
    mirror = [i[::-1] for i in mirror]
elif method == 3:
    mirror = mirror[::-1]
print("\n".join(map(str, mirror)))