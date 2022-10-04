from itertools import combinations
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(n)]
queue = []
c_list = []
for i in range(n):
    for j in range(n):
        if d[i][j] == 1:
            queue.append((i,j))
        elif d[i][j] == 2:
            c_list.append((i,j))

picks = list(combinations(c_list, m))
result = [0]*len(picks)

for x,y in queue:
    for i in range(len(picks)):
        temp = sys.maxsize
        for x1,y1 in picks[i]:
            distance = abs(x-x1) + abs(y-y1)
            temp = min(temp, distance)
        result[i] += temp
print(min(result))

# bfs 시간초과
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# d = [list(map(int, input().split())) for _ in range(n)]

# c = sum([row.count(2) for row in d])
# def bfs():
#     total = 0
#     queue = []
#     c_list = []
#     for i in range(n):
#         for j in range(n):
#             if d[i][j] == 1:
#                 queue.append((i,j))
#             elif d[i][j] == 2:
#                 c_list.append((i,j))

#     while queue:
#         x, y = queue.pop(0)
#         temp = []
#         for c in c_list:
#             x1, y1 = c
#             temp.append(abs(x-x1)+abs(y-y1))
#         total += min(temp)
    
#     return total

# def quit(cnt):
#     if cnt == c-m:
#         total = bfs()
#         result.append(total)
    
#     for i in range(n):
#         for j in range(n):
#             if d[i][j] == 2:
#                 d[i][j] = 0
#                 quit(cnt+1)
#                 d[i][j] = 2
# result = []
# quit(0)
# print(min(result))
