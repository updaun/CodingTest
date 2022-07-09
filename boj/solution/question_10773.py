import sys
input = sys.stdin.readline
n = int(input())
cal = []
for i in range(n):
    input_num = int(input())
    if input_num == 0:
        if len(cal) != 0:
            cal.pop()
    else:
        cal.append(input_num)
print(sum(cal))