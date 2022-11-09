# 비트 마스킹 풀이(68ms)
n = int(input())
bit = 0
while n > 0:
    n &= (n-1)
    bit += 1
print(bit)

# 이진수 변환 후 1 개수 세기(76ms)
n = int(input())
print(bin(n)[2:].count("1"))


# combinations 풀이(76ms)
from itertools import combinations
n = int(input())
s_list = [64]
while n < sum(s_list):
    select = s_list.pop(0)
    s_list.append(select//2)
while n != sum(s_list):
    if s_list[-1]//2 == 0:
        break
    s_list.append(s_list[-1]//2)

for i in range(len(s_list), 0, -1):
    for c in combinations(s_list, i):
        if n == sum(c):
            print(len(c))
            break
