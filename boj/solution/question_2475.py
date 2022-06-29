import sys
answer = 0
for num in list(map(int, sys.stdin.readline().split())):
    answer += num**2
print(answer%10)