n_list = list(map(int, input().split()))
temp = 1
while len([i for i in n_list if temp%i==0]) < 3:
    temp += 1
print(temp)