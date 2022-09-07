n = int(input())
temp = 1
time = 0
while n != 0:
    if n >= temp:
        n -= temp
        temp += 1
        time += 1
    else:
        temp = 1
print(time)
