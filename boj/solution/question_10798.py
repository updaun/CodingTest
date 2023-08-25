# 내 풀이(any, deque)
# from collections import deque
# s_list = []
# for i in range(5):
#     s_list.append(deque([i for i in input().strip()]))
# result = ""
# while any(s for s in s_list):
#     for i in range(5):
#         if s_list[i]:
#             result += s_list[i].popleft()
# print(result)

# 다른 사람 풀이(zip_longest)
from itertools import zip_longest

s_list = [input().strip() for _ in range(5)]
result = ""

for items in zip_longest(*s_list, fillvalue=''):
    result += ''.join(items)

print(result)
