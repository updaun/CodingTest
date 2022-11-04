import sys
input = sys.stdin.readline

def mul(a, b):
    n = len(a)
    result = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k]*b[k][j]
            result[i][j] %= 1000
    return result

def pow(origin, n):
    if n == 1:
        return origin
    if n % 2 == 0:
        temp = pow(origin, n//2)
        return mul(temp, temp)
    else:
        temp = pow(origin, n-1)
        return mul(temp, origin)

n, b = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
result = pow(a, b)
for row in result:
    for num in row:
        print(num % 1000, end=" ")
    print()