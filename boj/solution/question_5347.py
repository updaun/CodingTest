def gcd(a, b):
    while b:
        b, a = a%b, b
    return a
for i in range(int(input())):
    a, b = map(int, input().split())
    print(a*b//gcd(a,b))
