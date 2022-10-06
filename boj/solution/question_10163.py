# https://rrecoder.tistory.com/184 풀이 참고
n = int(input())
paper = []

for i in range(n):
    paper.append(list(map(int,input().split())))

place = [[0]*1001 for _ in range(1001)]

for i,p in enumerate(paper):
    [row,col,area,height] = p
    # 줄 단위 삽입으로 시간 단축
    for r in range(row,row+area):
        place[r][col:col+height] = [i+1]*height

for i in range(n):
    cnt=0
    for p in place:
        cnt += p.count(i+1)
    print(cnt)

# 시간초과
# import sys
# input = sys.stdin.readline
# n = int(input())
# d = [[0]*1001 for i in range(1001)]
# minx, miny = 1001, 1001
# maxx, maxy = 0, 0
# for t in range(n):
#     x, y, w, h = map(int, input().split())
#     for i in range(x, x+w):
#         for j in range(y, y+h):
#             d[i][j] = t+1
#     minx, miny = min(x, minx), min(y, miny)
#     maxx, maxy = max(x + w, maxx), max(y + h, maxy)
# result = [0]*(n+1)
# for k in range(1, n+1):
#     for i in range(minx, maxx):
#         for j in range(miny, maxy):
#             if d[i][j] == k:
#                 result[k] += 1
# print("\n".join(map(str, result[1:])))


# 시간초과
# import sys
# input = sys.stdin.readline
# n = int(input())
# d = [[0]*1001 for i in range(1001)]
# for t in range(n):
#     x, y, w, h = map(int, input().split())
#     for i in range(x, x+w):
#         for j in range(y, y+h):
#             d[i][j] = t+1
# result = [0]*n
# for i in range(n):
#     for row in d:
#         result[i] += row.count(i+1)
# print("\n".join(map(str, result)))
