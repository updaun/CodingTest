import sys
input = sys.stdin.readline

n, k = map(int, input().split())
d = [list(map(int, input().split())) for i in range(n)]
dp = [0] * (k+1)

for i in range(n):
    w, v = d[i]
    for j in range(k, w-1, -1):
        dp[j] = max(dp[j], dp[j-w]+v)
print(dp[-1])

# 시간 초과
# import sys
# from itertools import combinations
# input = sys.stdin.readline

# n, k = map(int, input().split())
# d = [list(map(int, input().split())) for i in range(n)]
# d.sort(key=lambda x:(x[0], -x[1]))
# temp = 0
# for i in range(1, len(d)+1):
    
#     for t in list(combinations(d, i)):
#         weight, value = 0, 0
#         for w, v in t:
#             weight += w
#             value += v
#             if weight > k:
#                 weight, value = 0, 0
#         temp = max(temp, value)
# print(temp)