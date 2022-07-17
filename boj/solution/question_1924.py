import sys
x, y = map(int, sys.stdin.readline().split())
days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
target = 0
month = {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}
for i in range(1, x):
    target += month[i]
target += y
print(days[target%7])