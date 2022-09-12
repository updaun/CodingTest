import sys
input = sys.stdin.readline

def is_prime(n):
    a = [False, True] + [True]*(n-1)
    for i in range(2,n+1):
        if a[i]:
            for j in range(2*i, n+1, i):
                a[j] = False
    return a[n]

alphabet = 'abcdefghijklmnopqrstuvwxyz'
d = {}
for i in range(len(alphabet)):
    d[alphabet[i]] = i+1
    d[alphabet[i].upper()] = len(alphabet) + i+1

input_str = input().rstrip()
result = 0
for s in input_str:
    result += d[s]

if is_prime(result):
    print("It is a prime word.")
else:
    print("It is not a prime word.")