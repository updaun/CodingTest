memo = [1, 1]
def fibo(n):
    if n < len(memo):
        return memo[n]
    else:
        value = fibo(n-1)+fibo(n-2)
        memo.append(value)
        return value

n = int(input())
if n == 1:
    print(0, 1)
elif n == 2:
    print(1, 1)
else:
    print(fibo(n-2), fibo(n-1))
        