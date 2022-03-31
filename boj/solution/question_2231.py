n = int(input())
target = n
while n > 0:
    n -= 1
    if "0" not in [i for i in str(n)] and target == n + sum([int(i) for i in str(n)]):
        break
print(n)
