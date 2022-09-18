# list comprehension 적용 속도 개선
# 308ms
import sys
input = sys.stdin.readline
n =  int(input())
m_list = [list(map(int, input().split())) for _ in range(n)]
m_list = sorted(m_list, key=lambda x:(x[1], x[0]))
count = 1
now = m_list[0][1]
for i in range(1, n):
    if m_list[i][0] >= now:
        count += 1
        now = m_list[i][1]
print(count)

# 옛날 풀이
# 328ms
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