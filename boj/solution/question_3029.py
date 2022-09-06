import sys

input = sys.stdin.readline

b = list(map(int, input().split(":")))
a = list(map(int, input().split(":")))

b_time = b[0]*3600 + b[1]*60 + b[2]
a_time = a[0]*3600 + a[1]*60 + a[2]

if a_time < b_time:
    temp = 86400 - b_time
    result = temp + a_time
elif a_time == b_time:
    result = 86400
else:
    result = a_time - b_time

h, result = divmod(result, 3600)
m, s = divmod(result,60)
print(f"{str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}")
