n = int(input())
temp = True
while n != 1:
    if n % 2 != 0:
        temp = False
        break
    else:
        n /= 2    
print(int(temp))