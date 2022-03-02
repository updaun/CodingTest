# n = int(input())
# a = 0
# b = 1
# direction = True
# for i in range(1, n+1):
#     if direction:
#         if b == 1:
#             a += 1
#             direction = False
#         else:
#             a += 1
#             b -= 1
#     else:
#         if a == 1:
#             b += 1
#             direction = True
#         else:
#             b += 1
#             a -= 1
# print(f'{str(a)}/{str(b)}')
'''
for 문을 사용하면 시간 초과 발생
'''
import math
n = int(input())
g = (-1 + math.sqrt(1+8*n)) / 2
u = math.ceil(g)
position = g - int(g)
if int(g) % 2 == 0:
    print(f'{u-int(int(g)*position)}/{1+int(int(g)*position)}')
else:
    print(f'{1+int(int(g)*position)}/{u-int(int(g)*position)}')
