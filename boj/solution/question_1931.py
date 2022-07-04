import sys
n = int(sys.stdin.readline())
schedules = []
for i in range(n):
    schedules.append(list(map(int, sys.stdin.readline().split())))
result = []
meetings = sorted(schedules, key=lambda x:(x[1], x[0]))
count = 1
start = meetings[0][1]
for idx in range(1, len(meetings)):
    meeting = meetings[idx]
    if start <= meeting[0]:
        count += 1
        start = meeting[1]
print(count)

# 시간초과
# import sys
# n = int(sys.stdin.readline())
# schedules = []
# for i in range(n):
#     schedules.append(list(map(int, sys.stdin.readline().split())))
# result = []
# meetings = sorted(schedules, key=lambda x:(x[0], x[1]))
# for i in range(int(len(meetings)/2)):
#     count = 0
#     start = 0
#     temp = meetings[i:]
#     for idx in range(len(temp)):
#         meet = temp[idx]
#         if start <= meet[0]:
#             count += 1
#             start = meet[1]
#     result.append(count)
# print(max(result))