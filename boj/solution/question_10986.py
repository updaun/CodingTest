import sys
N, M = map(int,sys.stdin.readline().split())
target = list(map(int,sys.stdin.readline().split()))
dp = [0 for i in range(M)]
temp = 0
dp[0] = 1
for i in range(N):
    temp+=target[i]
    dp[temp%M] += 1
ans=0
for i in dp:
    ans += i*(i-1)//2
print(ans)

# 시간 초과
# import sys
# N, M = list(map(int, sys.stdin.readline().split()))
# target = list(map(int, sys.stdin.readline().split()))
# count = 0
# for i in range(1, N):
#     for num in range(N):
#         if num+i <= N:
#             temp = sum(target[num:num+i])
#             if temp != 0 and temp % M == 0:
#                 count += 1
# if sum(target) % M == 0:
#     count +=1
# print(count)