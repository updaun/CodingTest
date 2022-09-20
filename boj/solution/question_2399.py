# 참고 https://aerocode.net/231
import sys
input = sys.stdin.readline
n = int(input())
n_list = sorted(list(map(int, input().split())))
result = 0
for i in range(n):
    result += n_list[i] * (2*i-n+1)
print(result*2)


# 시간 초과
# import sys
# input = sys.stdin.readline
# n = int(input())
# n_list = list(map(int, input().split()))
# result = 0
# for i in range(n-1, 0, -1):
#     for j in range(i):
#         result += abs(n_list[n-i-1]-n_list[n-i+j])
# print(result*2)


# 시간 초과
# import sys
# input = sys.stdin.readline
# n = int(input())
# n_list = list(map(int, input().split()))
# result = 0
# for i in range(n):
#     for j in range(n):
#         if i != j and i>j:
#             result += abs(n_list[i]-n_list[j])
# print(result*2)