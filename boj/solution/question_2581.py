M = int(input())
N = int(input())
sum_val = 0
min_val = N
for num in range(M, N+1):
    div = num-1
    flag = False
    if num == 1:
        continue
    while div > 1:
        if num % div == 0:
            flag = True
            break
        div -= 1
    if flag == False:
        sum_val += num
        if min_val > num:
            min_val = num
if sum_val != 0:
    print(sum_val)
    print(min_val)
else:
    print(-1)