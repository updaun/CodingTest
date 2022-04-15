fibo_list = []
for i in range(41):
    if i <= 0:
        fibo_list.append(0)
    elif i == 1:
        fibo_list.append(1)
    else:
        fibo_list.append(fibo_list[i-1]+fibo_list[i-2])
n = int(input())
n_list = []
for i in range(n):
    n_list.append(int(input()))
for i in n_list:
    if i == 0:
        print("1 0")
    else:
        print(fibo_list[i-1], fibo_list[i])
