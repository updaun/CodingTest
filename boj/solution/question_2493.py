# https://ywtechit.tistory.com/204
import sys
input = sys.stdin.readline
n = int(input())
t = list(map(int, input().split()))
result = [0 for i in range(n)]
stack = []
for i in range(n):
    while stack:
        if stack[-1][1] > t[i]:
            result[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, t[i]])
print(*result)


# 시간 초과
# import sys
# input = sys.stdin.readline
# n = int(input())
# t = list(map(int, input().split()))
# result = [0]
# for i in range(1, n):
#     for j in range(1, i):
#         if t[i-j] >= t[i]:
#             result.append(i-j+1)
#             break
#     else:
#         result.append(0)
# print(*result)