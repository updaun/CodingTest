import sys
input = sys.stdin.readline
n, m = map(int, input().split())
student = dict()
for i in range(n):
    student[i+1] = []
for i in range(m):
    a, b = map(int, input().split())
    student[a].append(b)
    student[b].append(a)
for i in range(1, n+1):
    print(len(student[i]))