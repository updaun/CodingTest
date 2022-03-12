n = int(input())
div = 2
while n > div:
    if n % div != 0:
        div += 1
    else:
        print(div)
        n = n / div
        div = 2
if n != 1:
    print(int(n))