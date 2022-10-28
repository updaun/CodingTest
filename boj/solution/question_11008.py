import sys
input = sys.stdin.readline
for _ in range(int(input())):
    s, p = input().split()
    print(len(s)+s.count(p)*(-len(p)+1))
    