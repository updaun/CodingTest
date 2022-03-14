# 시간초과 발생
# target_list = []

# while True:
#     n = int(input())
#     if n == 0:
#         break
#     else:
#         target_list.append(n)

# for n in target_list:
#     a = [False, False] + [True]*n*2
#     primes = []
#     cnt = 0
#     for i in range(2, 2*n+1):
#         if a[i]:
#             primes.append(i)
#         for j in range(2*i, 2*n+1, i):
#             a[j] = False
#     for prime in primes:
#         if prime > n:
#             cnt += 1
#     print(cnt)

# for n in range((123456*2))

# 문제의 범위까지 소수 리스트 생성
q_range = 123456*2
a = [False, False] + [True]*(q_range)
primes = []
for i in range(2, q_range):
    if a[i]:
        primes.append(i)
    for j in range(2*i, q_range, i):
        a[j] = False

target_list = []

while True:
    n = int(input())
    if n == 0:
        break
    else:
        target_list.append(n)

for n in target_list:
    count = 0
    for i in primes:
        if n < i <= 2*n:
            count += 1
    print(count)    

