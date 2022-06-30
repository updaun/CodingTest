n = int(input())
val = [0, 1]
count = 0
def fibonacci(n):
    global count
    count += 1
    if n >= 2:
        for i in range(2, n+1):
            val.append(val[i-2]+val[i-1])
    return val[n]
print(fibonacci(n), n-2)