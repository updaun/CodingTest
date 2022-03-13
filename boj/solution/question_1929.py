# 일반 소수 찾기 -> 시간초과
# M, N = tuple(map(int, input().split(" ")))

# def isprime(num):
#     div = 2
#     if num == 1:
#         return True
#     while num > div:
#         if num % div == 0:
#             return False
#         div += 1
#     return True

# for i in range(M, N+1):
#     if isprime(i):
#         print(i)

# 에라토스테네스의 체로 구현
M, N = tuple(map(int, input().split(" ")))

a = [False,False] + [True]*(N-1)
primes=[]

for i in range(2,N+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, N+1, i):
        a[j] = False
for i in primes:
    if i >= M:
        print(i)
