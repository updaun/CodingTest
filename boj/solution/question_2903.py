n = int(input())
temp = 2
for i in range(n):
    temp = temp+temp-1
print(temp**2)