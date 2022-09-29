import sys
input = sys.stdin.readline
k, n = map(int, input().split())
n_list = [int(input()) for i in range(k)]
start, end = 1, max(n_list)
count = 0
while start <= end:
    mid = (start + end) // 2
    count = 0 
    for line in n_list:
        count += line // mid
    if count >= n:
        start = mid +1
    else:
        end = mid -1
print(end)

# 시간초과
# import sys
# input = sys.stdin.readline
# k, n = map(int, input().split())
# n_list = [int(input()) for i in range(k)]
# temp = int(sum(n_list)/n)
# count = 0
# while True:
#     count = 0 
#     for line in n_list:
#         count += line // temp
#     if count == n:
#         print(temp)
#         break
#     temp -= 1
    