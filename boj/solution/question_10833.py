import sys
n = int(sys.stdin.readline())
remain = 0
for i in range(n):
    student, apple = list(map(int, sys.stdin.readline().split()))
    remain += apple % student
print(remain)