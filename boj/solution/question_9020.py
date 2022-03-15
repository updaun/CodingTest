q_range = 10000
a = [False, False] + [True]*(q_range)
primes = []
for i in range(2, q_range):
    if a[i]:
        primes.append(i)
    for j in range(2*i, q_range, i):
        a[j] = False

c = int(input())
target_list = []
for i in range(c):
    n = int(input())
    target_list.append(n)

for n in target_list:
    p = n//2 
    while p not in primes or n-p not in primes:
        p -= 1
    else:
        print(p, n-p)