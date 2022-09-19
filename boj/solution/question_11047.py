# 속도개선 68ms
import sys
input = sys.stdin.readline
c_num, value = map(int, input().split())
coin_list = [int(input()) for i in range(c_num)]
count = 0
for c in coin_list[::-1]:
    if c <= value:
        temp, value = divmod(value, c)
        count += temp
print(count)

# 72ms
# import sys
# n, k = list(map(int, sys.stdin.readline().split()))
# coin_list = []
# for i in range(n):
#     coin_list.append(int(sys.stdin.readline()))

# count = 0
# for i in coin_list[::-1]:
#     if k >= i:
#         count += k//i
#         k = k%i
#     if k == 0:
#         break
# print(count)