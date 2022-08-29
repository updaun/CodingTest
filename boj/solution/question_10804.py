import sys
input = sys.stdin.readline
c = [i+1 for i in range(20)]
for i in range(10):
    a, b = map(int, input().split())
    c = c[:a-1]+c[a-1:b][::-1]+c[b:]
print(" ".join(map(str, c)))