import sys
D, M = map(int, sys.stdin.readline().split())
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
target = 3
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(1, M):
    target += month[i]
target += D
print(days[target%7])