d, k = map(int, input().split())

def fibo(n):
    val = [0, 1]
    if n >= 2:
        for i in range(2, n+1):
            val.append(val[i-1]+val[i-2])
    return val[n]

a, b = fibo(d-2), fibo(d-1)
temp = 1
while ((k-a*temp)/b)%1!=0:
    temp +=1
print(temp)
print(int(((k-a*temp)/b)))

# 시간 초과
# import sys
# d, k = map(int, input().split())
# x1, y1 = 1, 0
# x2, y2 = 1, 1
# temp1, temp2 = 0, 0
# for i in range(1, d+1):
#     if i == 1:
#         x, y = x1, y1
#     elif i == 2:
#         x, y = x2, y2
#     else:
#         x = x1+x2
#         y = y1+y2
#         x1, y1 = x2, y2
#         x2, y2 = x, y
# for i in range(1, k+1):
#     for j in range(1, k+1):
#         if i <= j:
#             if x*i+y*j == k:
#                 print(i)
#                 print(i+j)
#                 sys.exit(0)