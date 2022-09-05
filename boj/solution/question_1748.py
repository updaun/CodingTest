n = int(input())
t = len(str(n))
result = 0
while t != 0:
    result += n - 10**(t-1) + 1
    t -= 1
print(result)
