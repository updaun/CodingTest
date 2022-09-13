# n = int(input())
# n_list = sorted(list(map(int, input().split())), reverse=True)
# temp = []
# result = 0
# for i in range(n):
#     if len(n_list) == 1:
#         temp = n_list+temp
#     elif i%2 == 0:
#         temp.append(n_list.pop(0))
#     else:
#         temp.append(n_list.pop())
# for i in range(1, n):
#     result += abs(temp[i-1]-temp[i])
# print(result)

from itertools import permutations
n = int(input())
n_list = list(map(int, input().split()))
result = 0
for temp in permutations(n_list):
    result_temp = 0
    for i in range(1, n):
        result_temp += abs(temp[i-1]-temp[i])
    result = max(result, result_temp)
print(result)